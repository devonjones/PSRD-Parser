#!/bin/bash
source dir.conf
rm $DATA_DIR/psrd.db
cp -r ../structure/* ../local
./json_loader.py -d $DATA_DIR/psrd.db -p "Spells" $DATA_DIR/core_rulebook/spells/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Spells" $DATA_DIR/advanced_players_guide/spells/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Spells" $DATA_DIR/ultimate_magic/spells/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Spells" $DATA_DIR/ultimate_combat/spells/*.json
./spell_list_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/core_rulebook/spell_lists/*.json
./spell_list_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_players_guide/spell_lists/*.json
./spell_list_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_magic/spell_lists/*.json
./spell_list_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_combat/spell_lists/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Races"    $DATA_DIR/*/races/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Skills"   $DATA_DIR/*/skills/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Feats"    $DATA_DIR/*/feats/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Classes"  $DATA_DIR/*/classes/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Monsters" $DATA_DIR/*/creatures/*.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ogl/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/core_rulebook/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_players_guide/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_combat/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_magic/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/game_mastery_guide/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_2/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_3/structure.json
./index_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/index.json

