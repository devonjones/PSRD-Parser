#!/bin/bash
./spell_list_parse.py -o ../data/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../data/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../data/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../data/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

