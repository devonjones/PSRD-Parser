#!/bin/bash
./feat_parse.py -o ../local/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../local/ -b "Bestiary"                ../web/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
#./feat_parse.py -o ../local/ -b "Bestiary 2"                ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/monsterFeats.html
./feat_parse.py -o ../local/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

