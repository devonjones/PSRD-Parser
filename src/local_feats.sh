#!/bin/bash
./feat_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../local/ -b "Bestiary"                ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
./feat_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

