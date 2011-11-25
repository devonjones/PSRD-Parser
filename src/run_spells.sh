#!/bin/bash
./spell_parse.py -o ../data/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../data/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../data/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../data/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

