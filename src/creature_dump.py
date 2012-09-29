#!/usr/bin/env python
import json
import jsonschema
import os.path
import pprint
import sys
from psrd.options import load_option_parser, exec_load_main
from psrd.sql import fetch_immediate_subordinantes, find_section, get_db_connection
from psrd.sql.creatures import fetch_creature_detail, fetch_creature_spells

CONF_DIR = os.path.join(os.path.dirname(__file__), '..', 'conf')

# TODO: Split?
# TODO: Cast to int?
# TODO: Link?
# TODO: Show causes?
# TODO: Deal with nulls?

def gen_source(creature):
	key = 'source'
	data = creature[key]
	del creature[key]
	return data

def gen_url(creature):
	key = 'url'
	data = creature[key]
	del creature[key]
	return data

def gen_name(creature):
	key = 'name'
	data = creature[key]
	del creature[key]
	return data

def gen_description(creature):
	key = 'description'
	data = creature[key]
	del creature[key]
	return data

def gen_cr(creature_details):
	key = 'cr'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_xp(creature_details):
	key = 'xp'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_sex(creature_details):
	key = 'sex'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_super_race(creature_details):
	key = 'super_race'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_level(creature_details):
	key = 'level'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_alignment(creature_details):
	key = 'alignment'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_size(creature_details):
	key = 'size'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_hit_dice(creature_details):
	key = 'hit_dice'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_creature_type(creature_details):
	key = 'creature_type'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_creature_subtype(creature_details):
	key = 'creature_subtype'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_init(creature_details):
	key = 'init'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_senses(creature_details):
	key = 'senses'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_aura(creature_details):
	key = 'aura'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_ac(creature_details):
	key = 'ac'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_hp(creature_details):
	key = 'hp'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_fortitude(creature_details):
	key = 'fortitude'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_reflex(creature_details):
	key = 'reflex'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_will(creature_details):
	key = 'will'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_defensive_abilities(creature_details):
	key = 'defensive_abilities'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_dr(creature_details):
	key = 'dr'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_immune(creature_details):
	key = 'immune'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_weaknesses(creature_details):
	key = 'weaknesses'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_sr(creature_details):
	key = 'sr'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_natural_armor(creature_details):
	key = 'natural_armor'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_resist(creature_details):
	key = 'resist'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_speed(creature_details):
	key = 'speed'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_melee(creature_details):
	key = 'melee'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_ranged(creature_details):
	key = 'ranged'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_breath_weapon(creature_details):
	key = 'breath_weapon'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_space(creature_details):
	key = 'space'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_reach(creature_details):
	key = 'reach'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_special_attacks(creature_details):
	key = 'special_attacks'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_spells(creature_spells):
	data = []
	for spell in creature_spells:
		tmp = {}
		tmp['name'] = spell['name']
		del spell['name']
		tmp['body'] = spell['body']
		del spell['body']
		data.append(tmp)
	return data

def gen_strength(creature_details):
	key = 'strength'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_dexterity(creature_details):
	key = 'dexterity'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_constitution(creature_details):
	key = 'constitution'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_intelligence(creature_details):
	key = 'intelligence'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_wisdom(creature_details):
	key = 'wisdom'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_charisma(creature_details):
	key = 'charisma'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_base_attack(creature_details):
	key = 'base_attack'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_cmb(creature_details):
	key = 'cmb'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_cmd(creature_details):
	key = 'cmd'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_feats(creature_details):
	key = 'feats'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_skills(creature_details):
	key = 'skills'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_racial_modifiers(creature_details):
	key = 'racial_modifiers'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_languages(creature_details):
	key = 'languages'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_special_qualities(creature_details):
	key = 'special_qualities'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_gear(creature_details):
	key = 'gear'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_environment(creature_details):
	key = 'environment'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_organization(creature_details):
	key = 'organization'
	data = creature_details[key]
	del creature_details[key]
	return data

def gen_treasure(creature_details):
	key = 'treasure'
	data = creature_details[key]
	del creature_details[key]
	return data

def output_creature(conn, creature_name):
	curs = conn.cursor()

	find_section(curs, name=creature_name)
	creatures = curs.fetchall()
	assert len(creatures) == 1
	creature = creatures[0]
	assert creature['type'] == 'creature'
	#pprint.pprint(creature)

	fetch_creature_detail(curs, creature['section_id'])
	creature_details = curs.fetchone()
	#pprint.pprint(creature_details)

	fetch_creature_spells(curs, creature['section_id'])
	creature_spells = curs.fetchall()
	#pprint.pprint(creature_spells)

	data = {}
	#	META
	data['source'] = gen_source(creature)
	data['url'] = gen_url(creature)
	data['name'] = gen_name(creature)
	data['description'] = gen_description(creature)
	#	BASE
	data['cr'] = gen_cr(creature_details)
	data['xp'] = gen_xp(creature_details)
	data['sex'] = gen_sex(creature_details)
	data['super_race'] = gen_super_race(creature_details)
	data['level'] = gen_level(creature_details)
	data['alignment'] = gen_alignment(creature_details)
	data['size'] = gen_size(creature_details)
	data['hit_dice'] = gen_hit_dice(creature_details)
	data['creature_type'] = gen_creature_type(creature_details)
	data['creature_subtype'] = gen_creature_subtype(creature_details)
	data['init'] = gen_init(creature_details)
	data['senses'] = gen_senses(creature_details)
	data['aura'] = gen_aura(creature_details)
	#	DEFENSE
	data['ac'] = gen_ac(creature_details)
	data['hp'] = gen_hp(creature_details)
	data['saves'] = {}
	data['saves']['fortitude'] = gen_fortitude(creature_details)
	data['saves']['reflex'] = gen_reflex(creature_details)
	data['saves']['will'] = gen_will(creature_details)
	data['defensive_abilities'] = gen_defensive_abilities(creature_details)
	data['dr'] = gen_dr(creature_details)
	data['immune'] = gen_immune(creature_details)
	data['weaknesses'] = gen_weaknesses(creature_details)
	data['sr'] = gen_sr(creature_details)
	data['natural_armor'] = gen_natural_armor(creature_details)
	data['resist'] = gen_resist(creature_details)
	#	OFFENSE
	data['speed'] = gen_speed(creature_details)
	data['melee'] = gen_melee(creature_details)
	data['ranged'] = gen_ranged(creature_details)
	data['breath_weapon'] = gen_breath_weapon(creature_details)
	data['space'] = gen_space(creature_details)
	data['reach'] = gen_reach(creature_details)
	data['special_attacks'] = gen_special_attacks(creature_details)
	data['spells'] = gen_spells(creature_spells)
	#	STATISTICS
	data['abilities'] = {}
	data['abilities']['strength'] = gen_strength(creature_details)
	data['abilities']['dexterity'] = gen_dexterity(creature_details)
	data['abilities']['constitution'] = gen_constitution(creature_details)
	data['abilities']['intelligence'] = gen_intelligence(creature_details)
	data['abilities']['wisdom'] = gen_wisdom(creature_details)
	data['abilities']['charisma'] = gen_charisma(creature_details)
	data['base_attack'] = gen_base_attack(creature_details)
	data['cmb'] = gen_cmb(creature_details)
	data['cmd'] = gen_cmd(creature_details)
	data['feats'] = gen_feats(creature_details)
	data['skills'] = gen_skills(creature_details)
	data['racial_modifiers'] = gen_racial_modifiers(creature_details)
	data['languages'] = gen_languages(creature_details)
	data['special_qualities'] = gen_special_qualities(creature_details)
	data['gear'] = gen_gear(creature_details)
	#	ECOLOGY
	data['environment'] = gen_environment(creature_details)
	data['organization'] = gen_organization(creature_details)
	data['treasure'] = gen_treasure(creature_details)
	#	SPECIAL ABILITIES
	# TODO
	#	TEXT
	# TODO

	del creature['create_index']
	del creature['lft']
	del creature['parent_id']
	del creature['rgt']
	del creature['section_id']
	del creature['abbrev'] # is null for all the creatures we have in the database
	del creature['alt'] # is null for all the creatures we have in the database
	del creature['body'] # only has value for seven creatures; what should we do with it?
	# sqlite> select name, body from sections where type = 'creature' and body is not  null;
	# Swarm, Bat|<StatBlockSection Special Features [(u'Wounding (Ex)', u'Any living creature damaged by a bat swarm continues to bleed, losing 1 hit point per round thereafter. Multiple wounds do not result in cumulative bleeding loss. The bleeding can be stopped by a DC 10 Heal check or the application of a cure spell or some other healing magic.')]>
	# Bat, Mobat|<p>XP 800	</p>
	# Blindheim|<p>Init +2; <b>Senses</b> darkvision 60 ft., low-light vision; <b>Perception</b> +9</p>
	# Daemon, Piscodaemon|<p><span class="char-style-override-30">XP</span> 9,600</p>
	# Daemon, Purrodaemon|<p><span class="char-style-override-30">XP</span> 153,600</p>
	# Fetchling|<p>Fetchling rogue 1</p>
	# Werebear (Hybrid Form)|<p>Human natural werebear ranger 4</p>
	del creature['image'] # is null for all the creatures we have in the database
	del creature['subtype'] # is null or familiar
	del creature['type']
	assert creature == {}

	del creature_details['creature_details_id']
	del creature_details['section_id']
	assert creature_details == {}

	for spell in creature_spells:
		del spell['creature_spells_id']
		del spell['section_id']
		assert spell == {}

	schema = json.load(open(os.path.join(CONF_DIR, 'creature_level1.json'), 'r'))
	jsonschema.validate(data, schema)

	pprint.pprint(data)

def output_creatures(db, args, parent):
	# parent means nothing in this case
	conn = get_db_connection(db)
	for arg in args:
		output_creature(conn, arg)

def main():
	usage = "usage: %prog [options] [creature]\nGenerate Creature Level 1 JSON output."
	# TODO: Accept a level option.
	parser = load_option_parser(usage)
	exec_load_main(parser, output_creatures)

if __name__ == "__main__":
	sys.exit(main())

