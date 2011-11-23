import json
from psrd.sql import get_db_connection
from psrd.universal import print_struct
from psrd.sections import cap_words
from psrd.sql import find_section, fetch_top, append_child_section, fetch_section, update_section
from psrd.sql.abilities import insert_ability_type
from psrd.sql.classes import insert_class_detail
from psrd.sql.feats import insert_feat_type, insert_feat_type_description
from psrd.sql.skills import insert_skill_attribute
from psrd.sql.spells import insert_spell_detail, update_spell_detail, insert_spell_list, fetch_spell_lists, insert_spell_descriptor, insert_spell_component, fetch_spell_components, insert_spell_effect, fetch_complete_spell, merge_spells

class ProcessLastException(Exception):
	def __init__(self, value):
		self.parameter = value

	def __str__(self):
		return repr(self.parameter)

def fetch_parent(curs, parent_name):
	if not parent_name:
		return fetch_top(curs)
	else:
		find_section(curs, name=parent_name, section_type='list')
		parent = curs.fetchone()
		if parent:
			return parent
		else:
			top = fetch_top(curs)
			section_id = append_child_section(curs, top['section_id'], 'list', None, parent_name, None, 'PFSRD', None, None)
			fetch_section(curs, section_id)
			return curs.fetchone()
		
def load_documents(db, args, parent):
	conn = get_db_connection(db)
	last = []
	for arg in args:
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
		sec_id = append_child_section(curs, parent_id, section['type'], section.get('subtype'), section.get('name'), section.get('abbrev'), section.get('source'), section.get('description'), section.get('text'))
		section['section_id'] = sec_id
		insert_subrecords(curs, section, sec_id)
		for s in section.get('sections', []):
			insert_section(curs, sec_id, s)
		return sec_id

def insert_subrecords(curs, section, section_id):
	if section['type'] == 'feat':
		if section.has_key('feat_types'):
			for feat_type in section['feat_types']:
				insert_feat_type(curs, section_id, feat_type)
			desc = "(" + ", ".join(section['feat_types']) + ")"
			insert_feat_type_description(curs, section_id, desc)
		else:
			insert_feat_type(curs, section_id, 'General')
			insert_feat_type_description(curs, section_id, "(General)")
	elif section['type'] == 'skill':
		insert_skill_attribute(curs, section_id, attribute=section['attribute'], armor_check_penalty=section.get('armor_check_penalty'), trained_only=section.get('trained_only'))
	elif section['type'] == 'ability':
		for ability_type in section['ability_types']:
			insert_ability_type(curs, section_id, ability_type)
	elif section['type'] == 'spell':
		insert_spell_records(curs, section_id, section)
	elif section['type'] == 'class':
		insert_class_detail(curs, section_id, section.get('alignment'), section.get('hit_die'))

def insert_spell_records(curs, section_id, spell):
	if spell.has_key('parent'):
		orig = fetch_complete_spell(curs, spell['parent'])
		if not orig:
			raise ProcessLastException(spell['parent'])
		spell = merge_spells(orig, spell)
	descriptor_text = ', '.join(spell.get('descriptor', []))
	if descriptor_text == "":
		descriptor_text = None
	level_list = []
	for level in spell.get('level', []):
		level_list.append(level['class'] + ": " + str(level['level']))
	level_text = "; ".join(level_list)
	insert_spell_detail(curs, section_id, spell.get('school'), spell.get('subschool'), descriptor_text, level_text, spell.get('casting_time'), spell.get('preparation_time'), spell.get('range'), spell.get('duration'), spell.get('saving_throw'), spell.get('spell_resistance'), spell.get('as_spell_id'))
	for descriptor in spell.get('descriptor', []):
		insert_spell_descriptor(curs, section_id, descriptor)
	for level in spell.get('level', []):
		magic_type = find_magic_type(level['class'])
		insert_spell_list(curs, section_id, level['level'], level['class'], magic_type)
	for component in spell.get('components', []):
		insert_spell_component(curs, section_id, component['type'], component.get('text'), 0)
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
		find_section(curs, name=name, section_type='spell')
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
		elif spell['name'].lower() == "planarbinding, lesser":
			newspells.append(_rename_spell("Planar Binding, Lesser", spell))
		elif spell['name'].lower() == "planarbinding, greater":
			newspells.append(_rename_spell("Planar Binding, Greater", spell))
		elif spell['name'] == "Lend Greater Judgment":
			newspells.append(_rename_spell("Lend Judgment, Greater", spell))
		elif spell['name'] == "Corruptionresistance":
			newspells.append(_rename_spell("Corruption Resistance", spell))
		elif spell['name'] == "Cat'sgrace, Mass":
			newspells.append(_rename_spell("Cat's Grace, Mass", spell))
		elif spell['name'] == "Fox'scunning, Mass":
			newspells.append(_rename_spell("Fox's Cunning, Mass", spell))
		elif spell['name'] == "Unwillingshield":
			newspells.append(_rename_spell("Unwilling Shield", spell))
		elif spell['name'] == "Banishseeming":
			newspells.append(_rename_spell("Banish Seeming", spell))
		elif spell['name'] == "Sharedwrath":
			newspells.append(_rename_spell("Shared Wrath", spell))
		elif spell['name'] == "Greater Magic Weapon":
			newspells.append(_rename_spell("Magic Weapon, Greater", spell))
		elif spell['name'] in ("Vermin Shape II", "Interrogation, Greater", "Lightning Rod"): # This is really fucked up, get ot it later.
			pass
		else:
			newspells.append(spell)
	struct['spells'] = newspells
	return struct

def _rename_spell(name, spell):
	newspell = spell.copy()
	newspell['name'] = name
	return newspell
