#!/bin/bash
./feat_parse.py -o ../data/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../data/ -b "Bestiary"                ../web/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
#./feat_parse.py -o ../data -b "Bestiary 2"                ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/monsterFeats.html
./feat_parse.py -o ../data/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../data/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../data/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

