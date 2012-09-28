#!/usr/bin/env python
import os
import os.path
import unittest
from creature_dump import (gen_ac, gen_alignment, gen_aura, gen_base_attack, gen_breath_weapon, gen_charisma,
		gen_cmb, gen_cmd, gen_constitution, gen_cr, gen_creature_type, gen_creature_subtype,
		gen_defensive_abilities, gen_description, gen_dexterity, gen_dr, gen_environment, gen_feats,
		gen_fortitude, gen_gear, gen_hit_dice, gen_hp, gen_immune, gen_init, gen_intelligence, gen_languages,
		gen_level, gen_melee, gen_name, gen_natural_armor, gen_organization, gen_racial_modifiers, gen_ranged,
		gen_reach, gen_reflex, gen_resist, gen_senses, gen_sex, gen_size, gen_skills, gen_source, gen_space,
		gen_special_attacks, gen_special_qualities, gen_speed, gen_spells, gen_sr, gen_strength, gen_super_race,
		gen_treasure, gen_url, gen_weaknesses, gen_will, gen_wisdom, gen_xp)
from psrd.sql import get_db_connection
from psrd.sql.creatures import fetch_creature_detail, fetch_creature_spells

# TODO: Assert that value.strip() is not the empty string?

class TestGenFunctions(unittest.TestCase):

	def setUp(self):
		self.db = os.path.join(os.getenv('DATA_DIR'), 'psrd.db')
		self.conn = get_db_connection(self.db)
		self.curs = self.conn.cursor()

	def tearDown(self):
		self.curs.close()
		self.curs = None
		self.conn.close()
		self.conn = None
		self.db = None

	def fetch_creatures(self):
		# TODO: Rework and move under psrd/sql.
		curs2 = self.conn.cursor()
		sqla = [
			'SELECT s.*',
			' FROM sections s',
			' WHERE s.type = ?',
		]
		sql = '\n'.join(sqla)
		values = ['creature']
		curs2.execute(sql, values)
		for row in curs2:
			yield row

	def test_gen_source(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			self.assertTrue('source' in creature, creature)
			source = gen_source(creature)
			#print source
			self.assertTrue('source' not in creature, creature)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_url(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			self.assertTrue('url' in creature, creature)
			url = gen_url(creature)
			#print url
			self.assertTrue('url' not in creature, creature)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_name(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			self.assertTrue('name' in creature, creature)
			name = gen_name(creature)
			#print name
			self.assertTrue('name' not in creature, creature)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_description(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			self.assertTrue('description' in creature, creature)
			description = gen_description(creature)
			#print description
			self.assertTrue('description' not in creature, creature)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_cr(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('cr' in creature_details, creature_details)
			cr = gen_cr(creature_details)
			#print cr
			self.assertTrue('cr' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_xp(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('xp' in creature_details, creature_details)
			xp = gen_xp(creature_details)
			#print xp
			self.assertTrue('xp' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_sex(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('sex' in creature_details, creature_details)
			sex = gen_sex(creature_details)
			#print sex
			self.assertTrue('sex' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_super_race(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('super_race' in creature_details, creature_details)
			super_race = gen_super_race(creature_details)
			#print super_race
			self.assertTrue('super_race' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_level(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('level' in creature_details, creature_details)
			level = gen_level(creature_details)
			#print level
			self.assertTrue('level' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_alignment(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('alignment' in creature_details, creature_details)
			alignment = gen_alignment(creature_details)
			#print alignment
			self.assertTrue('alignment' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_size(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('size' in creature_details, creature_details)
			size = gen_size(creature_details)
			#print size
			self.assertTrue('size' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_hit_dice(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('hit_dice' in creature_details, creature_details)
			hit_dice = gen_hit_dice(creature_details)
			#print hit_dice
			self.assertTrue('hit_dice' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_creature_type(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('creature_type' in creature_details, creature_details)
			creature_type = gen_creature_type(creature_details)
			#print creature_type
			self.assertTrue('creature_type' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_creature_subtype(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('creature_subtype' in creature_details, creature_details)
			creature_subtype = gen_creature_subtype(creature_details)
			#print creature_subtype
			self.assertTrue('creature_subtype' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_init(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('init' in creature_details, creature_details)
			init = gen_init(creature_details)
			#print init
			self.assertTrue('init' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_senses(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('senses' in creature_details, creature_details)
			senses = gen_senses(creature_details)
			#print senses
			self.assertTrue('senses' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_aura(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('aura' in creature_details, creature_details)
			aura = gen_aura(creature_details)
			#print aura
			self.assertTrue('aura' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_ac(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('ac' in creature_details, creature_details)
			ac = gen_ac(creature_details)
			#print ac
			self.assertTrue('ac' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_hp(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('hp' in creature_details, creature_details)
			hp = gen_hp(creature_details)
			#print hp
			self.assertTrue('hp' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_fortitude(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('fortitude' in creature_details, creature_details)
			fortitude = gen_fortitude(creature_details)
			#print fortitude
			self.assertTrue('fortitude' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_reflex(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('reflex' in creature_details, creature_details)
			reflex = gen_reflex(creature_details)
			#print reflex
			self.assertTrue('reflex' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_will(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('will' in creature_details, creature_details)
			will = gen_will(creature_details)
			#print will
			self.assertTrue('will' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_defensive_abilities(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('defensive_abilities' in creature_details, creature_details)
			defensive_abilities = gen_defensive_abilities(creature_details)
			#print defensive_abilities
			self.assertTrue('defensive_abilities' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_dr(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('dr' in creature_details, creature_details)
			dr = gen_dr(creature_details)
			#print dr
			self.assertTrue('dr' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_immune(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('immune' in creature_details, creature_details)
			immune = gen_immune(creature_details)
			#print immune
			self.assertTrue('immune' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_weaknesses(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('weaknesses' in creature_details, creature_details)
			weaknesses = gen_weaknesses(creature_details)
			#print weaknesses
			self.assertTrue('weaknesses' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_sr(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('sr' in creature_details, creature_details)
			sr = gen_sr(creature_details)
			#print sr
			self.assertTrue('sr' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_natural_armor(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('natural_armor' in creature_details, creature_details)
			natural_armor = gen_natural_armor(creature_details)
			#print natural_armor
			self.assertTrue('natural_armor' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_resist(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('resist' in creature_details, creature_details)
			resist = gen_resist(creature_details)
			#print resist
			self.assertTrue('resist' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_speed(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('speed' in creature_details, creature_details)
			speed = gen_speed(creature_details)
			#print speed
			self.assertTrue('speed' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_melee(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('melee' in creature_details, creature_details)
			melee = gen_melee(creature_details)
			#print melee
			self.assertTrue('melee' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_ranged(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('ranged' in creature_details, creature_details)
			ranged = gen_ranged(creature_details)
			#print ranged
			self.assertTrue('ranged' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_breath_weapon(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('breath_weapon' in creature_details, creature_details)
			breath_weapon = gen_breath_weapon(creature_details)
			#print breath_weapon
			self.assertTrue('breath_weapon' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_space(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('space' in creature_details, creature_details)
			space = gen_space(creature_details)
			#print space
			self.assertTrue('space' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_reach(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('reach' in creature_details, creature_details)
			reach = gen_reach(creature_details)
			#print reach
			self.assertTrue('reach' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_special_attacks(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('special_attacks' in creature_details, creature_details)
			special_attacks = gen_special_attacks(creature_details)
			#print special_attacks
			self.assertTrue('special_attacks' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_spells(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_spells(self.curs, creature['section_id'])
			creature_spells = self.curs.fetchall()
			#print creature_spells
			for spell in creature_spells:
				self.assertTrue('name' in spell, spell)
				self.assertTrue('body' in spell, spell)
			spells = gen_spells(creature_spells)
			#print spells
			for spell in creature_spells:
				self.assertTrue('name' not in spell, spell)
				self.assertTrue('body' not in spell, spell)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_strength(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('strength' in creature_details, creature_details)
			strength = gen_strength(creature_details)
			#print strength
			self.assertTrue('strength' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_dexterity(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('dexterity' in creature_details, creature_details)
			dexterity = gen_dexterity(creature_details)
			#print dexterity
			self.assertTrue('dexterity' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_constitution(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('constitution' in creature_details, creature_details)
			constitution = gen_constitution(creature_details)
			#print constitution
			self.assertTrue('constitution' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_intelligence(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('intelligence' in creature_details, creature_details)
			intelligence = gen_intelligence(creature_details)
			#print intelligence
			self.assertTrue('intelligence' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_wisdom(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('wisdom' in creature_details, creature_details)
			wisdom = gen_wisdom(creature_details)
			#print wisdom
			self.assertTrue('wisdom' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_charisma(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('charisma' in creature_details, creature_details)
			charisma = gen_charisma(creature_details)
			#print charisma
			self.assertTrue('charisma' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_base_attack(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('base_attack' in creature_details, creature_details)
			base_attack = gen_base_attack(creature_details)
			#print base_attack
			self.assertTrue('base_attack' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_cmb(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('cmb' in creature_details, creature_details)
			cmb = gen_cmb(creature_details)
			#print cmb
			self.assertTrue('cmb' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_cmd(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('cmd' in creature_details, creature_details)
			cmd = gen_cmd(creature_details)
			#print cmd
			self.assertTrue('cmd' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_feats(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('feats' in creature_details, creature_details)
			feats = gen_feats(creature_details)
			#print feats
			self.assertTrue('feats' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_skills(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('skills' in creature_details, creature_details)
			skills = gen_skills(creature_details)
			#print skills
			self.assertTrue('skills' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_racial_modifiers(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('racial_modifiers' in creature_details, creature_details)
			racial_modifiers = gen_racial_modifiers(creature_details)
			#print racial_modifiers
			self.assertTrue('racial_modifiers' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_languages(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('languages' in creature_details, creature_details)
			languages = gen_languages(creature_details)
			#print languages
			self.assertTrue('languages' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_special_qualities(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('special_qualities' in creature_details, creature_details)
			special_qualities = gen_special_qualities(creature_details)
			#print special_qualities
			self.assertTrue('special_qualities' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_gear(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('gear' in creature_details, creature_details)
			gear = gen_gear(creature_details)
			#print gear
			self.assertTrue('gear' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_environment(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('environment' in creature_details, creature_details)
			environment = gen_environment(creature_details)
			#print environment
			self.assertTrue('environment' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_organization(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('organization' in creature_details, creature_details)
			organization = gen_organization(creature_details)
			#print organization
			self.assertTrue('organization' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

	def test_gen_treasure(self):
		counter = 0
		for creature in self.fetch_creatures():
			#print creature
			fetch_creature_detail(self.curs, creature['section_id'])
			creature_details = self.curs.fetchone()
			#print creature_details
			self.assertTrue('treasure' in creature_details, creature_details)
			treasure = gen_treasure(creature_details)
			#print treasure
			self.assertTrue('treasure' not in creature_details, creature_details)
			counter += 1

		self.assertTrue(counter >= 966, counter)

if __name__ == '__main__':
	unittest.main()

