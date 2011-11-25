#!/bin/bash
mkdir -p ../local
rm -rf ../local/*

./class_parse.py -o ../local/ -c core     -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/classes/*.html
./class_parse.py -o ../local/ -c prestige -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/prestigeClasses/*.html
./class_parse.py -o ../local/ -c npc      -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/nPCClasses.html
./class_parse.py -o ../local/ -c base     -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/baseClasses/*.html
./class_parse.py -o ../local/ -c prestige -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/prestigeClasses/*.html
./class_parse.py -o ../local/ -c base     -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcasters/*.html
./class_parse.py -o ../local/ -c base     -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classes/*.html

./feat_parse.py -o ../local/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/feats.html
./feat_parse.py -o ../local/ -b "Bestiary"                ../web/paizo.com/pathfinderRPG/prd/monsters/monsterFeats.html
./feat_parse.py -o ../local/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicFeats.html
./feat_parse.py -o ../local/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatFeats.html

./race_parse.py -o ../local/ -b "Core Rulebook" ../web/paizo.com/pathfinderRPG/prd/races.html 

./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Getting Started"    ../web/paizo.com/pathfinderRPG/prd/gettingStarted.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Classes"            ../web/paizo.com/pathfinderRPG/prd/classes.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Using Skills"       ../web/paizo.com/pathfinderRPG/prd/usingSkills.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Skill Descriptions" ../web/paizo.com/pathfinderRPG/prd/skillDescriptions.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Equipment"          ../web/paizo.com/pathfinderRPG/prd/equipment.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Additional Rules"   ../web/paizo.com/pathfinderRPG/prd/additionalRules.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Combat"             ../web/paizo.com/pathfinderRPG/prd/combat.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Magic"              ../web/paizo.com/pathfinderRPG/prd/magic.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Prestige Classes"   ../web/paizo.com/pathfinderRPG/prd/prestigeClasses.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Gamemastering"      ../web/paizo.com/pathfinderRPG/prd/gamemastering.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Environment"        ../web/paizo.com/pathfinderRPG/prd/environment.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Creating NPCs"      ../web/paizo.com/pathfinderRPG/prd/creatingNPCs.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Magic Items"        ../web/paizo.com/pathfinderRPG/prd/magicItems.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Glossary"           ../web/paizo.com/pathfinderRPG/prd/glossary.html

./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Armor"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/armor.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Artifacts"             ../web/paizo.com/pathfinderRPG/prd/magicItems/artifacts.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Cursed Items"          ../web/paizo.com/pathfinderRPG/prd/magicItems/cursedItems.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Intelligent Items"     ../web/paizo.com/pathfinderRPG/prd/magicItems/intelligentItems.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Magic Item Creation"   ../web/paizo.com/pathfinderRPG/prd/magicItems/magicItemCreation.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Potions"               ../web/paizo.com/pathfinderRPG/prd/magicItems/potions.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Rings"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/rings.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Rods"                  ../web/paizo.com/pathfinderRPG/prd/magicItems/rods.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Scrolls"               ../web/paizo.com/pathfinderRPG/prd/magicItems/scrolls.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Specific Cursed Items" ../web/paizo.com/pathfinderRPG/prd/magicItems/specificCursedItems.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Staves"                ../web/paizo.com/pathfinderRPG/prd/magicItems/staves.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Wands"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/wands.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Weapons"               ../web/paizo.com/pathfinderRPG/prd/magicItems/weapons.html
./rules_parse.py -o ../local/ -b "Core Rulebook" -t "Wonderous Items"       ../web/paizo.com/pathfinderRPG/prd/magicItems/wondrousItems.html

./skill_parse.py -o ../local/ -b "Core Rulebook" ../web/paizo.com/pathfinderRPG/prd/skills/*.html

./spell_list_parse.py -o ../local/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/spellLists.html
./spell_list_parse.py -o ../local/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicSpellLists.html
./spell_list_parse.py -o ../local/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatSpellLists.html

./spell_parse.py -o ../local/ -b "Core Rulebook"           ../web/paizo.com/pathfinderRPG/prd/spells/*.html
./spell_parse.py -o ../local/ -b "Advanced Player's Guide" ../web/paizo.com/pathfinderRPG/prd/advanced/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Magic"          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spells/*.html
./spell_parse.py -o ../local/ -b "Ultimate Combat"         ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/spells/*.html

