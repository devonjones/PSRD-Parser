#!/bin/bash
set -e

source ./dir.conf
./feat_parse.py -o $DATA_DIR -b "Core Rulebook"           $WEB_DIR/pathfinderRPG/prd/feats.html
./feat_parse.py -o $DATA_DIR -b "Bestiary"                $WEB_DIR/pathfinderRPG/prd/monsters/monsterFeats.html
#./feat_parse.py -o $DATA_DIR -b "Bestiary 2"              $WEB_DIR/pathfinderRPG/prd/additionalMonsters/monsterFeats.html
./feat_parse.py -o $DATA_DIR -b "Advanced Class Guide"    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/feats.html
./feat_parse.py -o $DATA_DIR -b "Advanced Player's Guide" $WEB_DIR/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o $DATA_DIR -b "Ultimate Magic"          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o $DATA_DIR -b "Ultimate Combat"         $WEB_DIR/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html
./feat_parse.py -o $DATA_DIR -b "Ultimate Campaign"       $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/storyFeats.html
./feat_parse.py -o $DATA_DIR -b "Mythic Adventures"       $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicFeats.html
./feat_parse.py -o $DATA_DIR -b "Occult Adventures"       $WEB_DIR/pathfinderRPG/prd/occultAdventures/feats.html

