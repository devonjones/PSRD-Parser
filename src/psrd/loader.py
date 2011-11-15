import json
from psrd.sql import get_db_connection
from psrd.universal import print_struct
from psrd.sql import find_section, fetch_top, append_child_section, fetch_section
from psrd.sql.abilities import insert_ability_type
from psrd.sql.feats import insert_feat_type
from psrd.sql.skills import insert_skill_attribute
from psrd.sql.spells import insert_spell_detail, insert_spell_list, fetch_spell_lists, insert_spell_descriptor, insert_spell_component, fetch_spell_components, insert_spell_effect, fetch_complete_spell, merge_spells

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
		else:
			insert_feat_type(curs, section_id, 'General')
	elif section['type'] == 'skill':
		insert_skill_attribute(curs, section_id, attribute=section['attribute'], armor_check_penalty=section.get('armor_check_penalty'), trained_only=section.get('trained_only'))
	elif section['type'] == 'ability':
		for ability_type in section['ability_types']:
			insert_ability_type(curs, section_id, ability_type)
	elif section['type'] == 'spell':
		insert_spell_records(curs, section_id, section)

def insert_spell_records(curs, section_id, spell):
	if spell.has_key('parent'):
		orig = fetch_complete_spell(curs, spell['parent'])
		if not orig:
			raise ProcessLastException(spell['parent'])
		spell = merge_spells(orig, spell)
	insert_spell_detail(curs, section_id, spell.get('school'), spell.get('subschool'), spell.get('casting_time'), spell.get('preparation_time'), spell.get('range'), spell.get('duration'), spell.get('saving_throw'), spell.get('spell_resistance'), spell.get('as_spell_id'))
	for level in spell.get('levels', []):
		magic_type = 'arcane'
		if level['class'] in ['cleric', 'druid', 'parladin', 'ranger', 'oracle', 'inquisitor']:
			magic_type = 'divine'
		insert_spell_list(curs, section_id, level['level'], level['class'], magic_type)
	for component in spell.get('components', []):
		insert_spell_component(curs, section_id, component['type'], component.get('text'), 0)
	for descriptor in spell.get('descriptor', []):
		insert_spell_descriptor(curs, section_id, descriptor)
	for effect in spell.get('effects', []):
		insert_spell_effect(curs, section_id, effect['name'], effect['text'])
	
