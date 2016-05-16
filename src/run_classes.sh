#!/bin/bash
set -e

source ./dir.conf
./class_parse.py -o $DATA_DIR -c core     -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/classes/*.html
./class_parse.py -o $DATA_DIR -c prestige -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/prestigeClasses/*.html
./class_parse.py -o $DATA_DIR -c npc      -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/nPCClasses.html
./class_parse.py -o $DATA_DIR -c hybrid   -b "Advanced Class Guide"    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classes/*.html
./class_parse.py -o $DATA_DIR -c base     -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/baseClasses/*.html
./class_parse.py -o $DATA_DIR -c prestige -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/prestigeClasses/*.html
./class_parse.py -o $DATA_DIR -c base     -b "Ultimate Magic"          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcasters/*.html
./class_parse.py -o $DATA_DIR -c base     -b "Ultimate Combat"         $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classes/*.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/kineticist.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/medium.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/mesmerist.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/occultist.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/psychic.html
./class_parse.py -o $DATA_DIR -c base     -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/classes/spiritualist.html


