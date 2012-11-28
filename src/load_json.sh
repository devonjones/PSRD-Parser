#!/bin/bash

source dir.conf
rm $DATA_DIR/book*.db
rm $DATA_DIR/index.db
set -e
cp -r ../structure/* $DATA_DIR

# Core Rulebook
./json_loader.py       -d $DATA_DIR/book-cr.db -p "Spells"   $DATA_DIR/core_rulebook/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-cr.db               $DATA_DIR/core_rulebook/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-cr.db -p "Races"    $DATA_DIR/core_rulebook/races/*.json
./json_loader.py       -d $DATA_DIR/book-cr.db -p "Skills"   $DATA_DIR/core_rulebook/skills/*.json
./json_loader.py       -d $DATA_DIR/book-cr.db -p "Feats"    $DATA_DIR/core_rulebook/feats/*.json
./json_loader.py       -d $DATA_DIR/book-cr.db -p "Classes"  $DATA_DIR/core_rulebook/classes/*.json
./rules_loader.py      -d $DATA_DIR/book-cr.db               $DATA_DIR/core_rulebook/structure.json
./index_loader.py      -d $DATA_DIR/book-cr.db

# Advanced Player's Guide
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Spells"   $DATA_DIR/advanced_players_guide/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-apg.db               $DATA_DIR/advanced_players_guide/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Feats"    $DATA_DIR/advanced_players_guide/feats/*.json
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Classes"  $DATA_DIR/advanced_players_guide/classes/*.json
./rules_loader.py      -d $DATA_DIR/book-apg.db               $DATA_DIR/advanced_players_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-apg.db

# Ultimate Magic
./json_loader.py       -d $DATA_DIR/book-um.db -p "Spells"   $DATA_DIR/ultimate_magic/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-um.db               $DATA_DIR/ultimate_magic/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Feats"    $DATA_DIR/ultimate_magic/feats/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Classes"  $DATA_DIR/ultimate_magic/classes/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Monsters" $DATA_DIR/ultimate_magic/creatures/*.json
./rules_loader.py      -d $DATA_DIR/book-um.db               $DATA_DIR/ultimate_magic/structure.json
./index_loader.py      -d $DATA_DIR/book-um.db

# Ultimate Combat
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Spells"   $DATA_DIR/ultimate_combat/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-uc.db               $DATA_DIR/ultimate_combat/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Feats"    $DATA_DIR/ultimate_combat/feats/*.json
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Classes"  $DATA_DIR/ultimate_combat/classes/*.json
./rules_loader.py      -d $DATA_DIR/book-uc.db               $DATA_DIR/ultimate_combat/structure.json
./index_loader.py      -d $DATA_DIR/book-uc.db

# Advanced Race Guide
./spell_list_loader.py -d $DATA_DIR/book-arg.db               $DATA_DIR/advanced_race_guide/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-arg.db -p "Races"    $DATA_DIR/advanced_race_guide/races/*.json
./rules_loader.py      -d $DATA_DIR/book-arg.db               $DATA_DIR/advanced_race_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-arg.db

# Game Mastery Guide
./json_loader.py       -d $DATA_DIR/book-gmg.db -p "Monsters" $DATA_DIR/game_mastery_guide/creatures/*.json
./rules_loader.py      -d $DATA_DIR/book-gmg.db               $DATA_DIR/game_mastery_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-gmg.db

# Bestiary
./json_loader.py       -d $DATA_DIR/book-b1.db -p "Feats"    $DATA_DIR/bestiary_all/feats/*.json
./rules_loader.py      -d $DATA_DIR/book-b1.db               $DATA_DIR/bestiary_all/structure.json
./json_loader.py       -d $DATA_DIR/book-b1.db -p "Monsters" $DATA_DIR/bestiary/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b1.db

# Bestiary 2
./json_loader.py       -d $DATA_DIR/book-b2.db -p "Monsters" $DATA_DIR/bestiary_2/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b2.db

# Bestiary 3
./json_loader.py       -d $DATA_DIR/book-b3.db -p "Monsters" $DATA_DIR/bestiary_3/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b3.db

# Central Index
./central_index_loader.py   -d $DATA_DIR/index.db   $DATA_DIR/book-*.db
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/core_rulebook/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/advanced_players_guide/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/ultimate_magic/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/ultimate_combat/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/advanced_race_guide/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/game_mastery_guide/urlref.json
./url_ref_loader.py         -d $DATA_DIR/index.db   $DATA_DIR/bestiary_all/urlref.json
./menu_loader.py            -d $DATA_DIR/index.db   $DATA_DIR/menu.json

# OGL and Community Use License
./rules_loader.py      -d $DATA_DIR/book-ogl.db               $DATA_DIR/ogl/structure.json

echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-cr.db > $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-apg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-um.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-uc.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-arg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-gmg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b1.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b2.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b3.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/index.db >> $DATA_DIR/urllist.txt.tmp
cat $DATA_DIR/urllist.txt.tmp | sort > $DATA_DIR/urllist.txt
rm $DATA_DIR/urllist.txt.tmp

