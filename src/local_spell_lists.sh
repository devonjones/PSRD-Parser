#!/bin/bash
./spell_list_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

