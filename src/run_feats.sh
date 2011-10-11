#!/bin/bash
./feat_parse.py -o ../data/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../data/ -b "Bestiary" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
./feat_parse.py -o ../data/ -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../data/ -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../data/ -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

