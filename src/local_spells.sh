#!/bin/bash
source dir.conf
./spell_parse.py -o $DATA_DIR -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o $DATA_DIR -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o $DATA_DIR -b "Ultimate Magic"          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o $DATA_DIR -b "Ultimate Combat"         $WEB_DIR/pathfinderRPG/prd/ultimateCombat/spells/*.html

