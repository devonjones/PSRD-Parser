#!/bin/bash
./class_parse.py -o ../data/ -c core -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/classes/*.html
./class_parse.py -o ../data/ -c prestige -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/prestigeClasses/*.html
./class_parse.py -o ../data/ -c npc -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/nPCClasses.html
./class_parse.py -o ../data/ -c base -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/baseClasses/*.html
./class_parse.py -o ../data/ -c prestige -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/prestigeClasses/*.html
./class_parse.py -o ../data/ -c base -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcasters/*.html
./class_parse.py -o ../data/ -c base -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/classes/*.html

