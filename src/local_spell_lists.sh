#!/bin/bash
source dir.conf
./spell_list_parse.py -o $DATA_DIR -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Ultimate Magic"          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Ultimate Combat"         $WEB_DIR/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

