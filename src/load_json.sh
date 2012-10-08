#!/bin/bash

source dir.conf
rm $DATA_DIR/psrd.db
set -e
cp -r ../structure/* $DATA_DIR
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
./json_loader.py -d $DATA_DIR/psrd.db -p "Monsters" $DATA_DIR/bestiary/creatures/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Monsters" $DATA_DIR/bestiary_2/creatures/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Monsters" $DATA_DIR/bestiary_3/creatures/*.json
./json_loader.py -d $DATA_DIR/psrd.db -p "Monsters" $DATA_DIR/game_mastery_guide/creatures/*.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/core_rulebook/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_players_guide/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_race_guide/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_combat/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_magic/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/game_mastery_guide/structure.json
#./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary/structure.json
#./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_2/structure.json
#./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_3/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_all/structure.json
./rules_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ogl/structure.json
./index_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/index.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/core_rulebook/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_players_guide/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/advanced_race_guide/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_combat/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/ultimate_magic/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/game_mastery_guide/urlref.json
./url_ref_loader.py -d $DATA_DIR/psrd.db $DATA_DIR/bestiary_all/urlref.json

echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/psrd.db > $DATA_DIR/urllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/psrd.db >> $DATA_DIR/urllist.txt.tmp
cat $DATA_DIR/urllist.txt.tmp | sort > $DATA_DIR/urllist.txt
rm $DATA_DIR/urllist.txt.tmp

