#!/bin/bash
./class_parse.py -o ../data/ -c core     -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/classes/*.html
./class_parse.py -o ../data/ -c prestige -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/prestigeClasses/*.html
./class_parse.py -o ../data/ -c npc      -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/nPCClasses.html
./class_parse.py -o ../data/ -c base     -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/baseClasses/*.html
./class_parse.py -o ../data/ -c prestige -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/prestigeClasses/*.html
./class_parse.py -o ../data/ -c base     -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcasters/*.html
./class_parse.py -o ../data/ -c base     -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classes/*.html

