#!/bin/bash
set -e

source dir.conf
./spell_list_parse.py -o $DATA_DIR -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Advanced Class Guide"    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/spellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Ultimate Magic"          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Ultimate Combat"         $WEB_DIR/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Advanced Race Guide"     $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/spellLists.html
./spell_list_parse.py -o $DATA_DIR -b "Mythic Adventures"       $WEB_DIR/pathfinderRPG/prd/mythicAdventures/spellLists.html

