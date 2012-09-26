from animal_companion import is_animal_companion, parse_animal_companion
from creature import is_creature, parse_creature, is_npc, parse_npc
from spell import is_spell, parse_spell
from trap import is_trap, parse_trap
from affliction import is_affliction, parse_affliction
from item import is_item, parse_item
from creature_type import is_creature_type, parse_creature_type
from spellbook import is_spellbook, parse_spellbook
from vehicle import is_vehicle, parse_vehicle
from settlement import is_settlement, parse_settlement
from haunt import is_haunt, parse_haunt
from section import is_section, parse_section
from utils import StatBlockFunctions, parse_stat_block
from psrd.universal import StatBlockHeading

StatBlockFunctions().add_function(is_animal_companion, parse_animal_companion)
StatBlockFunctions().add_function(is_npc, parse_npc)
StatBlockFunctions().add_function(is_creature, parse_creature)
StatBlockFunctions().add_function(is_spell, parse_spell)
StatBlockFunctions().add_function(is_trap, parse_trap)
StatBlockFunctions().add_function(is_affliction, parse_affliction)
StatBlockFunctions().add_function(is_item, parse_item)
StatBlockFunctions().add_function(is_creature_type, parse_creature_type)
StatBlockFunctions().add_function(is_spellbook, parse_spellbook)
StatBlockFunctions().add_function(is_vehicle, parse_vehicle)
StatBlockFunctions().add_function(is_settlement, parse_settlement)
StatBlockFunctions().add_function(is_haunt, parse_haunt)
StatBlockFunctions().add_function(is_section, parse_section)
StatBlockFunctions().add_default(parse_section)

def stat_block_pass(section, book, no_sb=False):
	if section.__class__ == dict:
		if section.has_key('sections'):
			newsections = []
			for s in section['sections']:
				if s.__class__ == StatBlockHeading:
					newsections.append(parse_stat_block(s, book, no_sb=no_sb))
				elif s.__class__ == dict:
					newsections.append(stat_block_pass(s, book))
				else:
					newsections.append(s)
			section['sections'] = newsections
		return section
	return parse_stat_block(section, book, no_sb=no_sb)

