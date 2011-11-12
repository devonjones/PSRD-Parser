from psrd.universal import print_struct
from psrd.sql import find_section, fetch_top, append_child_section
from psrd.sql.abilities import insert_ability_type
from psrd.sql.feats import insert_feat_type
from psrd.sql.skills import insert_skill_attribute

def load_document(db, conn, filename, struct):
	curs = conn.cursor()
	try:
		top = fetch_top(curs)
		#find_section(curs, struct.get('name'), struct['type'], struct['source'])
		#sec = curs.fetchone()
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
