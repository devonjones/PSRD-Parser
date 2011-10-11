#!/bin/bash
./spell_parse.py -o ../local/ -b "Core Rulebook" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../local/ -b "Advanced Player's Guide" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Magic" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Combat" ../../../data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

