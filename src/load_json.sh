#!/bin/bash
./json_loader.py -d ../data/psrd.db -p "Spells" ../data/core_rulebook/spells/*.json
./json_loader.py -d ../data/psrd.db -p "Spells" ../data/advanced_players_guide/spells/*.json
./json_loader.py -d ../data/psrd.db -p "Spells" ../data/ultimate_magic/spells/*.json
./json_loader.py -d ../data/psrd.db -p "Spells" ../data/ultimate_combat/spells/*.json
./spell_list_loader.py -d ../data/psrd.db ../data/core_rulebook/spell_lists/*.json
./spell_list_loader.py -d ../data/psrd.db ../data/advanced_players_guide/spell_lists/*.json
./spell_list_loader.py -d ../data/psrd.db ../data/ultimate_magic/spell_lists/*.json
./spell_list_loader.py -d ../data/psrd.db ../data/ultimate_combat/spell_lists/*.json
./json_loader.py -d ../data/psrd.db -p "Races"   ../data/core_rulebook/races/*.json
./json_loader.py -d ../data/psrd.db -p "Skills"  ../data/core_rulebook/skills/*.json
./json_loader.py -d ../data/psrd.db -p "Feats"   ../data/core_rulebook/feats/*.json
./json_loader.py -d ../data/psrd.db -p "Classes" ../data/core_rulebook/classes/*.json
./json_loader.py -d ../data/psrd.db -p "Rules"   ../data/core_rulebook/rules/*.json
./json_loader.py -d ../data/psrd.db -p "Monsters" ../data/*/creatures/*.json
./rules_loader.py -d ../data/psrd.db ../data/ogl/structure.json
./rules_loader.py -d ../data/psrd.db ../data/core_rulebook/structure.json
./rules_loader.py -d ../data/psrd.db ../data/advanced_players_guide/structure.json
./rules_loader.py -d ../data/psrd.db ../data/ultimate_combat/structure.json
./rules_loader.py -d ../data/psrd.db ../data/ultimate_magic/structure.json
./rules_loader.py -d ../data/psrd.db ../data/game_mastery_guide/structure.json
./rules_loader.py -d ../data/psrd.db ../data/bestiary/structure.json
./rules_loader.py -d ../data/psrd.db ../data/bestiary_2/structure.json
./rules_loader.py -d ../data/psrd.db ../data/bestiary_3/structure.json
./index_loader.py -d ../data/psrd.db ../structure/index.json

