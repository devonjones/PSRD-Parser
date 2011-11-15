#!/bin/bash
./spell_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

