#!/bin/bash
./json_loader.py -d ../local/psrd.db -p "Spells" ../local/core_rulebook/spells/*.json
./json_loader.py -d ../local/psrd.db -p "Spells" ../local/advanced_players_guide/spells/*.json
./json_loader.py -d ../local/psrd.db -p "Spells" ../local/ultimate_magic/spells/*.json
./json_loader.py -d ../local/psrd.db -p "Spells" ../local/ultimate_combat/spells/*.json
./spell_list_loader.py -d ../local/psrd.db ../local/core_rulebook/spell_lists/*.json
./spell_list_loader.py -d ../local/psrd.db ../local/advanced_players_guide/spell_lists/*.json
./spell_list_loader.py -d ../local/psrd.db ../local/ultimate_magic/spell_lists/*.json
./spell_list_loader.py -d ../local/psrd.db ../local/ultimate_combat/spell_lists/*.json
./json_loader.py -d ../local/psrd.db -p "Races" ../local/*/races/*.json
./json_loader.py -d ../local/psrd.db -p "Skills" ../local/*/skills/*.json
./json_loader.py -d ../local/psrd.db -p "Feats" ../local/*/feats/*.json
./json_loader.py -d ../local/psrd.db -p "Classes" ../local/*/classes/*.json
./json_loader.py -d ../local/psrd.db -p "Monsters" ../local/*/creatures/*.json
./rules_loader.py -d ../local/psrd.db ../local/core_rulebook/structure.json
./rules_loader.py -d ../local/psrd.db ../local/advanced_players_guide/structure.json
./rules_loader.py -d ../local/psrd.db ../local/ultimate_combat/structure.json
./rules_loader.py -d ../local/psrd.db ../local/ultimate_magic/structure.json
./rules_loader.py -d ../local/psrd.db ../local/game_mastery_guide/structure.json
./rules_loader.py -d ../local/psrd.db ../local/bestiary/structure.json
./rules_loader.py -d ../local/psrd.db ../local/bestiary_2/structure.json
./rules_loader.py -d ../local/psrd.db ../local/bestiary_3/structure.json
./index_loader.py -d ../local/psrd.db ../structure/index.json

