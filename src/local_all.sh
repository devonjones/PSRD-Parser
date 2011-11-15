#!/bin/bash
mkdir -p ../local
rm -rf ../local/*

./class_parse.py -o ../local/ -c core     -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/classes/*.html
./class_parse.py -o ../local/ -c prestige -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/prestigeClasses/*.html
./class_parse.py -o ../local/ -c npc      -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/nPCClasses.html
./class_parse.py -o ../local/ -c base     -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/baseClasses/*.html
./class_parse.py -o ../local/ -c prestige -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/prestigeClasses/*.html
./class_parse.py -o ../local/ -c base     -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcasters/*.html
./class_parse.py -o ../local/ -c base     -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/classes/*.html

./feat_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../local/ -b "Bestiary"                ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
./feat_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

./race_parse.py -o ../local/ -b "Core Rulebook" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/races.html 

./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Getting Started"    ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/gettingStarted.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Classes"            ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/classes.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Using Skills"       ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/usingSkills.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Skill Descriptions" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/skillDescriptions.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Equipment"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/equipment.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Additional Rules"   ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/additionalRules.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Combat"             ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/combat.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Magic"              ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/magic.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Prestige Classes"   ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/prestigeClasses.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Gamemastering"      ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/gamemastering.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Environment"        ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/environment.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Creating NPCs"      ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/creatingNPCs.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Magic Items"        ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/magicItems.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Glossary"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/glossary.html

./skill_parse.py -o ../local/ -b "Core Rulebook" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/skills/*.html

./spell_list_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

./spell_parse.py -o ../local/ -b "Core Rulebook"           ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../local/ -b "Advanced Player's Guide" ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Magic"          ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Combat"         ~/Unison/data/websites/Pathfinder\ psrd/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

