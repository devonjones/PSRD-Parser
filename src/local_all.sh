#!/bin/bash
mkdir -p ../local
rm -rf ../local/*

./core_class_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/classes/*.html

./feat_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../local/ -b "Bestiary" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
./feat_parse.py -o ../local/ -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

./race_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/races.html 

./skill_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/skills/*.html

./spell_list_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../local/ -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

./spell_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../local/ -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

