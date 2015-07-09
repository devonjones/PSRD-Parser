from psrd.sql.abilities import fetch_ability_type
from psrd.sql.afflictions import fetch_affliction_detail
from psrd.sql.animal_companions import fetch_animal_companion_detail
from psrd.sql.armies import fetch_army_detail
from psrd.sql.classes import fetch_class_detail
from psrd.sql.creatures import fetch_creature_detail, fetch_creature_spells
from psrd.sql.feats import fetch_feat_types
from psrd.sql.haunts import fetch_haunt_detail
from psrd.sql.items import fetch_item_detail, fetch_item_misc
from psrd.sql.kingdom_resources import fetch_kingdom_resource_detail
from psrd.sql.mythic_spells import fetch_mythic_spell_detail
from psrd.sql.resources import fetch_resource_detail
from psrd.sql.settlements import fetch_settlement_detail
from psrd.sql.skills import fetch_skill_attribute
from psrd.sql.spells import fetch_spell_detail, fetch_spell_lists, fetch_spell_subschools, fetch_spell_descriptors, fetch_spell_components, fetch_spell_effects
from psrd.sql.traps import fetch_trap_detail
from psrd.sql.vehicles import fetch_vehicle_detail

def handle_abilities(conn, section):
	curs = conn.cursor()
	try:
		fetch_ability_type(curs, section['section_id'])
		ability_types = []
		for ability_type in curs.fetchall():
			del ability_type['ability_type_id']
			del ability_type['section_id']
			ability_types.append(ability_type['ability_type'])
		if len(ability_types) > 0:
			section['ability_types'] = ability_type
	finally:
		curs.close()

def handle_affliction(conn, section):
	curs = conn.cursor()
	try:
		fetch_affliction_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['affliction_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_animal_companion(conn, section):
	curs = conn.cursor()
	try:
		fetch_animal_companion_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['animal_companion_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_army(conn, section):
	curs = conn.cursor()
	try:
		fetch_army_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['army_detail_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_class(conn, section):
	curs = conn.cursor()
	try:
		fetch_class_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['class_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_creature(conn, section):
	curs = conn.cursor()
	try:
		fetch_creature_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['creature_details_id']
			del detail['section_id']
			section.update(detail)
		fetch_creature_spells(curs, section['section_id'])
		spells = []
		for spell in curs.fetchall():
			spells.append({spell['name']: spell['body']})
		if len(spells) > 0:
			section['spells'] = spells
	finally:
		curs.close()

def handle_feat(conn, section):
	curs = conn.cursor()
	try:
		fetch_feat_types(curs, section['section_id'])
		feat_types = []
		for feat_type in curs.fetchall():
			del feat_type['feat_type_id']
			del feat_type['section_id']
			feat_types.append(feat_type['feat_type'])
		if len(feat_types) > 0:
			section['feat_types'] = feat_type
	finally:
		curs.close()

def handle_haunt(conn, section):
	curs = conn.cursor()
	try:
		fetch_haunt_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['haunt_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_item(conn, section):
	curs = conn.cursor()
	try:
		fetch_item_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['item_details_id']
			del detail['section_id']
			section.update(detail)
		fetch_item_misc(curs, section['section_id'])
		item_misc = {}
		for misc in curs.fetchall():
			subsection = item_misc.setdefault(misc['subsection'], {})
			subsection[misc['field']] = misc['value']
		if len(item_misc) > 0:
			section['misc'] = item_misc
	finally:
		curs.close()

def handle_kingdom_resource(conn, section):
	curs = conn.cursor()
	try:
		fetch_kingdom_resource_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['kingdom_resource_detail_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_mythic_spell(conn, section):
	curs = conn.cursor()
	try:
		fetch_mythic_spell_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['spell_detail_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_resource(conn, section):
	curs = conn.cursor()
	try:
		fetch_resource_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['resource_detail_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_settlement(conn, section):
	curs = conn.cursor()
	try:
		fetch_settlement_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['settlement_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_skill(conn, section):
	curs = conn.cursor()
	try:
		fetch_skill_attribute(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['skill_attribute_id']
			del detail['section_id']
			if detail['armor_check_penalty']:
				detail['armor_check_penalty'] = True
			else:
				detail['armor_check_penalty'] = True
			if detail['trained_only']:
				detail['trained_only'] = True
			else:
				detail['trained_only'] = True
			section.update(detail)
	finally:
		curs.close()

def handle_spell(conn, section):
	curs = conn.cursor()
	try:
		fetch_spell_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['spell_detail_id']
			del detail['section_id']
			section.update(detail)
		fetch_spell_lists(curs, section['section_id'])
		levels = []
		for level in curs.fetchall():
			levels.append({"class": level['class'], "level": level['level']})
		if len(levels) > 0:
			section['levels'] = levels
		fetch_spell_subschools(curs, section['section_id'])
		subschools = []
		for subschool in curs.fetchall():
			subschools.append(subschool['subschool'])
		if len(subschools) > 0:
			section['subschool'] = subschools
		fetch_spell_descriptors(curs, section['section_id'])
		descriptors = []
		for descriptor in curs.fetchall():
			descriptors.append(descriptor['descriptor'])
		if len(descriptors) > 0:
			section['descriptor'] = descriptors
		fetch_spell_effects(curs, section['section_id'])
		effects = []
		for effect in curs.fetchall():
			effects.append({'name': effect['name'], 'text': effect['description']})
		if len(effects) > 0:
			section['effects'] = effects
		fetch_spell_components(curs, section['section_id'])
		components = []
		for component in curs.fetchall():
			c = {"type": component['component_type']}
			if component['description']:
				c['text'] = component['description']
			components.append(c)
		if len(components) > 0:
			section['components'] = components
	finally:
		curs.close()

def handle_trap(conn, section):
	curs = conn.cursor()
	try:
		fetch_trap_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['trap_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def handle_vehicle(conn, section):
	curs = conn.cursor()
	try:
		fetch_vehicle_detail(curs, section['section_id'])
		detail = curs.fetchone()
		if detail:
			del detail['vehicle_details_id']
			del detail['section_id']
			section.update(detail)
	finally:
		curs.close()

def fetch_subrecords(conn, section):
	handlers = {
		'ability': handle_abilities,
		'affliction': handle_affliction,
		'animal_companion': handle_animal_companion,
		'army': handle_army,
		'class': handle_class,
		'creature': handle_creature,
		'feat': handle_feat,
		'haunt': handle_haunt,
		'item': handle_item,
		'kingdom_resource': handle_kingdom_resource,
		'mythic_spell': handle_mythic_spell,
		'resource': handle_resource,
		'settlement': handle_settlement,
		'skill': handle_skill,
		'spell': handle_spell,
		'trap': handle_trap,
		'vehicle': handle_vehicle,
	}
	if section['type'] in handlers:
		handlers[section['type']](conn, section)
