#!/bin/bash
./spell_list_parse.py -o ../data/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../data/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../data/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../data/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

