import json
import sys
import os
from psrd.sql import get_db_connection
from psrd.universal import print_struct
from psrd.sections import cap_words
from psrd.sql import find_section, fetch_top, append_child_section, fetch_section, update_section
from psrd.sql.abilities import insert_ability_type
from psrd.sql.afflictions import insert_affliction_detail
from psrd.sql.animal_companions import insert_animal_companion_detail
from psrd.sql.settlements import insert_settlement_detail
from psrd.sql.vehicles import insert_vehicle_detail
from psrd.sql.creatures import insert_creature_detail, insert_creature_spell
from psrd.sql.traps import insert_trap_detail
from psrd.sql.items import insert_item_detail
from psrd.sql.links import insert_link_detail
from psrd.sql.classes import insert_class_detail
from psrd.sql.feats import insert_feat_type, insert_feat_type_description
from psrd.sql.skills import insert_skill_attribute
from psrd.sql.spells import insert_spell_detail, update_spell_detail, insert_spell_list, fetch_spell_lists, insert_spell_descriptor, insert_spell_component, fetch_spell_components, insert_spell_effect, fetch_complete_spell, merge_spells

class ProcessLastException(Exception):
	def __init__(self, value):
		self.parameter = value

	def __str__(self):
		return repr(self.parameter)

def generate_url(curs, parent_id, name, create_index=True, parent_url=None):
	if not create_index:
		return
	if name is None:
		return
	name = name.replace(':', '')
	name = name.replace('&', 'and')
	name = name.replace('?', '')
	if parent_id == None:
		return "pfsrd://%s" % name
	if parent_url == None:
		p_id = parent_id
		while parent_url is None:
			find_section(curs, section_id=p_id)
			section = curs.fetchone()
			parent_url = section['url']
			p_id = section['parent_id']
	if name.find(', ') > -1:
		parent_chunks = parent_url.split('/')
		name_chunks = name.split(', ')
		merged = []
		while len(name_chunks) > 0:
			nc = name_chunks.pop()
			if nc == parent_chunks[-1]:
				parent_chunks.pop()
			merged.insert(0, nc)
		parent_chunks.extend(merged)
		result = '/'.join(parent_chunks)
		if result == parent_url:
			name_chunks = name.split(', ')
			parent_chunks.extend(merged)
			result = '/'.join(parent_chunks)
		return result
	return parent_url + "/" + name

def fetch_parent(curs, parent_name):
	if not parent_name:
		return fetch_top(curs)
	else:
		find_section(curs, name=parent_name, type='list')
		parent = curs.fetchone()
		if parent:
			return parent
		else:
			top = fetch_top(curs)
			section_id = append_child_section(curs, top['section_id'], 'list', None, parent_name, None, 'PFSRD', None, None, None, None, generate_url(curs, top['section_id'], parent_name), False)
			fetch_section(curs, section_id)
			return curs.fetchone()
		
def load_documents(db, args, parent):
	conn = get_db_connection(db)
	last = []
	for arg in args:
		print arg
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		try:
			load_document(db, conn, arg, struct, parent)
		except ProcessLastException, pe:
			conn.rollback()
			last.append((struct, arg))
	for struct, arg in last:
		load_document(db, conn, arg, struct, parent)

def load_document(db, conn, filename, struct, parent):
	curs = conn.cursor()
	try:
		top = fetch_parent(curs, parent)
		section_id = insert_section(curs, top['section_id'], struct)
		conn.commit()
	finally:
		curs.close()
	print_struct(struct)

def insert_section(curs, parent_id, section):
	if section['type'] == 'spell_list':
		add_spell_list(curs, section)
	else:
		sec_id = append_child_section(curs, parent_id, section['type'], section.get('subtype'), section.get('name'), section.get('abbrev'), section.get('source'), section.get('description'), section.get('text'), section.get('image'), section.get('alt'), generate_url(curs, parent_id, section.get('name'), create_index=section.get('create_index', True)), section.get('create_index'))
		section['section_id'] = sec_id
		insert_subrecords(curs, section, sec_id)
		for s in section.get('sections', []):
			insert_section(curs, sec_id, s)
		return sec_id

def _feat_insert(curs, section, section_id):
	if section.has_key('feat_types'):
		for feat_type in section['feat_types']:
			insert_feat_type(curs, section_id, feat_type)
		desc = "(" + ", ".join(section['feat_types']) + ")"
		insert_feat_type_description(curs, section_id, desc)
	else:
		insert_feat_type(curs, section_id, 'General')
		insert_feat_type_description(curs, section_id, "(General)")

def _skill_insert(curs, section, section_id):
	insert_skill_attribute(curs, section_id, attribute=section['attribute'], armor_check_penalty=section.get('armor_check_penalty'), trained_only=section.get('trained_only'))

def _ability_insert(curs, section, section_id):
	for ability_type in section['ability_types']:
		insert_ability_type(curs, section_id, ability_type)

def _spell_insert(curs, section, section_id):
	insert_spell_records(curs, section_id, section)

def _class_insert(curs, section, section_id):
	insert_class_detail(curs, section_id, section.get('alignment'), section.get('hit_dice'))

def _affliction_insert(curs, section, section_id):
	insert_affliction_detail(curs, **section)

def _animal_companion_insert(curs, section, section_id):
	insert_animal_companion_detail(curs, **section)

def _settlement_insert(curs, section, section_id):
	insert_settlement_detail(curs, **section)

def _vehicle_insert(curs, section, section_id):
	insert_vehicle_detail(curs, **section)

def _creature_insert(curs, section, section_id):
	insert_creature_detail(curs, **section)
	if section.has_key('spells'):
		spells = section['spells']
		for key in spells.keys():
			insert_creature_spell(curs, section_id, key, spells[key])

def _link_insert(curs, section, section_id):
	insert_link_detail(curs, section_id, section['url'], section.get('display', False))

def _trap_insert(curs, section, section_id):
	insert_trap_detail(curs, **section)

def _item_insert(curs, section, section_id):
	insert_item_detail(curs, **section)

def _noop(curs, section, section_id):
	pass

def insert_subrecords(curs, section, section_id):
	fxns = {
		"affliction": _affliction_insert,
		"feat": _feat_insert,
		"skill": _skill_insert,
		"ability": _ability_insert,
		"spell": _spell_insert,
		"class": _class_insert,
		"animal_companion": _animal_companion_insert,
		"settlement": _settlement_insert,
		"vehicle": _vehicle_insert,
		"creature": _creature_insert,
		"trap": _trap_insert,
		"item": _item_insert,
		"link": _link_insert,
		"table": _noop,
		"racial_trait": _noop,
		"section": _noop,
		"class_archetype": _noop,
	}
	if section['type'] in fxns:
		section['section_id'] = section_id
		fxns[section['type']](curs, section, section_id)
	else:
		sys.stderr.write("%s has no section type handler\n" % section['type'])

def insert_spell_records(curs, section_id, spell):
	if spell.has_key('parent'):
		orig = fetch_complete_spell(curs, spell['parent'])
		if not orig:
			raise ProcessLastException(spell['parent'])
		spell = merge_spells(orig, spell)
	descriptor_text = ', '.join(spell.get('descriptor', []))
	if descriptor_text == "":
		descriptor_text = None
	else:
		spell['descriptor_text'] = descriptor_text
	level_list = []
	for level in spell.get('level', []):
		level_list.append(level['class'] + ": " + str(level['level']))
	level_text = "; ".join(level_list)
	spell['level_text'] = level_text
	insert_spell_detail(curs, **spell)
	for descriptor in spell.get('descriptor', []):
		insert_spell_descriptor(curs, section_id, descriptor)
	for level in spell.get('level', []):
		magic_type = find_magic_type(level['class'])
		insert_spell_list(curs, section_id, level['level'], cap_words(level['class']), magic_type)
	for component in spell.get('components', []):
		insert_spell_component(curs, section_id, component.get('type'), component.get('text'), 0)
	for effect in spell.get('effects', []):
		insert_spell_effect(curs, section_id, effect['name'], effect['text'])

def find_magic_type(class_name):
	magic_type = 'arcane'
	if class_name.lower() in ['cleric', 'druid', 'paladin', 'ranger', 'oracle', 'inquisitor']:
		magic_type = 'divine'
	return magic_type

def load_spell_list_documents(db, args, parent):
	conn = get_db_connection(db)
	last = []
	for arg in args:
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		try:
			load_spell_list_document(db, conn, arg, struct, parent)
		except ProcessLastException, pe:
			conn.rollback()
			last.append((struct, arg))
	for struct, arg in last:
		load_document(db, conn, arg, struct, parent)

def load_spell_list_document(db, conn, filename, struct, parent):
	curs = conn.cursor()
	try:
		section_id = add_spell_list(curs, struct)
		conn.commit()
	finally:
		curs.close()
	print_struct(struct)

def add_spell_list(curs, struct):
	if not struct['type'] == 'spell_list':
		raise Exception("This should only be run on spell list files")
	if struct['class'] in ("Sorcerer/wizard", "Sorcerer/Wizard"):
		struct['class'] = "Sorcerer"
		add_spell_list(curs, struct)
		struct['class'] = "Wizard"
		add_spell_list(curs, struct)
		return
	struct = fix_spell_list(struct)
	level = struct['level']
	class_name = cap_words(struct['class'])
	for sp in struct['spells']:
		name = cap_words(sp['name'].strip())
		find_section(curs, name=name, type='spell')
		spell = curs.fetchone()
		if not spell:
			raise Exception("Cannot find spell %s" % name)
		fetch_spell_lists(curs, spell['section_id'], class_name=class_name)
		if not curs.fetchone():
			magic_type = find_magic_type(class_name.lower())
			insert_spell_list(curs, spell['section_id'], level, class_name, magic_type)
			fix_spell_level_text(curs, spell['section_id'])
		if sp.has_key('description'):
			update_section(curs, spell['section_id'], description=sp['description'])

def fix_spell_level_text(curs, section_id):
	fetch_spell_lists(curs, section_id)
	sl = []
	objs = curs.fetchall()
	for obj in objs:
		sl.append(obj['class'] + ": " + str(obj['level']))
	level_text = "; ".join(sl)
	update_spell_detail(curs, section_id, level_text=level_text)

def fix_spell_list(struct):
	spells = struct['spells']
	newspells = []
	for spell in spells:
		if spell['name'] == 'Magic Circle Vs Chaos/Evil/Good/Law':
			spell['name'] = 'Magic Circle Against Chaos/Evil/Good/Law'

		if spell['name'].find("Chaos/Evil/Good/Law") > -1:
			name = spell['name'].replace("Chaos/Evil/Good/Law", "")
			newspells.append(_rename_spell(name + "Chaos", spell))
			newspells.append(_rename_spell(name + "Evil", spell))
			newspells.append(_rename_spell(name + "Good", spell))
			newspells.append(_rename_spell(name + "Law", spell))
		elif spell['name'].find("Chaos/Evil") > -1:
			name = spell['name'].replace("Chaos/Evil", "")
			newspells.append(_rename_spell(name + "Chaos", spell))
			newspells.append(_rename_spell(name + "Evil", spell))
		elif spell['name'].find("Good/Law") > -1:
			name = spell['name'].replace("Good/Law", "")
			newspells.append(_rename_spell(name + "Good", spell))
			newspells.append(_rename_spell(name + "Law", spell))
		elif spell['name'] == "Dispel Magic, Greater Ethereal Jaunt":
			newspells.append(_rename_spell("Dispel Magic, Greater", spell))
			newspells.append(_rename_spell("Ethereal Jaunt", spell))
		elif spell['name'] == "Thunderous Drums":
			newspells.append(_rename_spell("Thundering Drums", spell))
		elif spell['name'] == "Lend Greater Judgment":
			newspells.append(_rename_spell("Lend Judgment, Greater", spell))
		elif spell['name'] == "Greater Magic Weapon":
			newspells.append(_rename_spell("Magic Weapon, Greater", spell))
		elif spell['name'] in ("Vermin Shape II", "Interrogation, Greater", "Lightning Rod"): # This is really fucked up, get to it later.
			pass
		else:
			newspells.append(spell)
	struct['spells'] = newspells
	return struct

def _rename_spell(name, spell):
	newspell = spell.copy()
	newspell['name'] = name
	return newspell

def process_structure_node(curs, filename, parent, struct):
	section = None
	if struct.has_key('file'):
		print struct['file']
		jsonfile = os.path.dirname(filename) + "/" + struct['file']
		fp = open(jsonfile, 'r')
		data = json.load(fp)
		fp.close()
		section_id = insert_section(curs, parent['section_id'], data)
		fetch_section(curs, section_id)
		section = curs.fetchone()
	else:
		find_section(curs, name=struct['name'], parent_id=parent['section_id'])
		section = curs.fetchone()
		if not section:
			section_id = append_child_section(curs, parent['section_id'], 'list', None, struct['name'], None, 'PFSRD', None, None, None, None, generate_url(curs, parent['section_id'], struct['name'], create_index=struct.get('create_index', True), parent_url=parent['url']), False)
			fetch_section(curs, section_id)
			section = curs.fetchone()
	for child in struct.get('children', []):
		process_structure_node(curs, filename, section, child)

def load_rule_structure_document(db, conn, filename, struct):
	curs = conn.cursor()
	try:
		find_section(curs, name=struct['name'])
		parent = curs.fetchone()
		if struct.has_key('file'):
			print struct['file']
		for child in struct['children']:
			process_structure_node(curs, filename, parent, child) 
		conn.commit()
	finally:
		curs.close()
	print_struct(struct)

def load_rule_structure_documents(db, args, parent):
	conn = get_db_connection(db)
	for arg in args:
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		load_rule_structure_document(db, conn, arg, struct)
