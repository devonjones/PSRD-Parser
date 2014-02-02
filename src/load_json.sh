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
./url_ref_loader.py    -d $DATA_DIR/book-cr.db               $DATA_DIR/core_rulebook/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-cr.db > $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-cr.db > $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-cr.db >> $DATA_DIR/urllist.txt.tmp

# Advanced Player's Guide
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Spells"   $DATA_DIR/advanced_players_guide/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-apg.db               $DATA_DIR/advanced_players_guide/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Feats"    $DATA_DIR/advanced_players_guide/feats/*.json
./json_loader.py       -d $DATA_DIR/book-apg.db -p "Classes"  $DATA_DIR/advanced_players_guide/classes/*.json
./rules_loader.py      -d $DATA_DIR/book-apg.db               $DATA_DIR/advanced_players_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-apg.db
./url_ref_loader.py    -d $DATA_DIR/book-apg.db               $DATA_DIR/advanced_players_guide/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-apg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-apg.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-apg.db >> $DATA_DIR/urllist.txt.tmp

# Ultimate Magic
./json_loader.py       -d $DATA_DIR/book-um.db -p "Spells"   $DATA_DIR/ultimate_magic/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-um.db               $DATA_DIR/ultimate_magic/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Feats"    $DATA_DIR/ultimate_magic/feats/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Classes"  $DATA_DIR/ultimate_magic/classes/*.json
./json_loader.py       -d $DATA_DIR/book-um.db -p "Monsters" $DATA_DIR/ultimate_magic/creatures/*.json
./rules_loader.py      -d $DATA_DIR/book-um.db               $DATA_DIR/ultimate_magic/structure.json
./index_loader.py      -d $DATA_DIR/book-um.db
./url_ref_loader.py    -d $DATA_DIR/book-um.db               $DATA_DIR/ultimate_magic/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-um.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-um.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-um.db >> $DATA_DIR/urllist.txt.tmp

# Ultimate Combat
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Spells"   $DATA_DIR/ultimate_combat/spells/*.json
./spell_list_loader.py -d $DATA_DIR/book-uc.db               $DATA_DIR/ultimate_combat/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Feats"    $DATA_DIR/ultimate_combat/feats/*.json
./json_loader.py       -d $DATA_DIR/book-uc.db -p "Classes"  $DATA_DIR/ultimate_combat/classes/*.json
./rules_loader.py      -d $DATA_DIR/book-uc.db               $DATA_DIR/ultimate_combat/structure.json
./index_loader.py      -d $DATA_DIR/book-uc.db
./url_ref_loader.py    -d $DATA_DIR/book-uc.db               $DATA_DIR/ultimate_combat/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-uc.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-uc.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-uc.db >> $DATA_DIR/urllist.txt.tmp

# Advanced Race Guide
./spell_list_loader.py -d $DATA_DIR/book-arg.db               $DATA_DIR/advanced_race_guide/spell_lists/*.json
./json_loader.py       -d $DATA_DIR/book-arg.db -p "Races"    $DATA_DIR/advanced_race_guide/races/*.json
./rules_loader.py      -d $DATA_DIR/book-arg.db               $DATA_DIR/advanced_race_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-arg.db
./url_ref_loader.py    -d $DATA_DIR/book-arg.db               $DATA_DIR/advanced_race_guide/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-arg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-arg.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-arg.db >> $DATA_DIR/urllist.txt.tmp

# Ultimate Equipment 
./rules_loader.py      -d $DATA_DIR/book-ue.db                $DATA_DIR/ultimate_equipment/structure.json
./index_loader.py      -d $DATA_DIR/book-ue.db
./url_ref_loader.py    -d $DATA_DIR/book-ue.db                $DATA_DIR/ultimate_equipment/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ue.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ue.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-ue.db >> $DATA_DIR/urllist.txt.tmp

# Ultimate Campaign
./rules_loader.py      -d $DATA_DIR/book-ucampaign.db                $DATA_DIR/ultimate_campaign/structure.json
./json_loader.py       -d $DATA_DIR/book-ucampaign.db -p "Feats"     $DATA_DIR/ultimate_campaign/feats/*.json
./index_loader.py      -d $DATA_DIR/book-ucampaign.db
./url_ref_loader.py    -d $DATA_DIR/book-ucampaign.db                $DATA_DIR/ultimate_campaign/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ucampaign.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ucampaign.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-ucampaign.db >> $DATA_DIR/urllist.txt.tmp

# Mythic Adventures
./json_loader.py       -d $DATA_DIR/book-ma.db -p "Feats"    $DATA_DIR/mythic_adventures/feats/*.json
./json_loader.py       -d $DATA_DIR/book-ma.db -p "Monsters" $DATA_DIR/mythic_adventures/creatures/*.json
./rules_loader.py      -d $DATA_DIR/book-ma.db               $DATA_DIR/mythic_adventures/structure.json
./index_loader.py      -d $DATA_DIR/book-ma.db
#./url_ref_loader.py    -d $DATA_DIR/book-ma.db               $DATA_DIR/mythic_adventures/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ma.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-ma.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-ma.db >> $DATA_DIR/urllist.txt.tmp

# Game Mastery Guide
./json_loader.py       -d $DATA_DIR/book-gmg.db -p "Monsters" $DATA_DIR/game_mastery_guide/creatures/*.json
./rules_loader.py      -d $DATA_DIR/book-gmg.db               $DATA_DIR/game_mastery_guide/structure.json
./index_loader.py      -d $DATA_DIR/book-gmg.db
./url_ref_loader.py    -d $DATA_DIR/book-gmg.db               $DATA_DIR/game_mastery_guide/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-gmg.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-gmg.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-gmg.db >> $DATA_DIR/urllist.txt.tmp

# Bestiary
./json_loader.py       -d $DATA_DIR/book-b1.db -p "Feats"    $DATA_DIR/bestiary_all/feats/*.json
./rules_loader.py      -d $DATA_DIR/book-b1.db               $DATA_DIR/bestiary_all/structure.json
./json_loader.py       -d $DATA_DIR/book-b1.db -p "Monsters" $DATA_DIR/bestiary/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b1.db
./url_ref_loader.py    -d $DATA_DIR/book-b1.db               $DATA_DIR/bestiary/urlref.json
./url_ref_loader.py    -d $DATA_DIR/book-b1.db               $DATA_DIR/bestiary_all/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b1.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b1.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-b1.db >> $DATA_DIR/urllist.txt.tmp

# Bestiary 2
./json_loader.py       -d $DATA_DIR/book-b2.db -p "Monsters" $DATA_DIR/bestiary_2/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b2.db
./url_ref_loader.py    -d $DATA_DIR/book-b2.db               $DATA_DIR/bestiary_2/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b2.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b2.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-b2.db >> $DATA_DIR/urllist.txt.tmp

# Bestiary 3
./json_loader.py       -d $DATA_DIR/book-b3.db -p "Monsters" $DATA_DIR/bestiary_3/creatures/*.json
./index_loader.py      -d $DATA_DIR/book-b3.db
./url_ref_loader.py    -d $DATA_DIR/book-b3.db               $DATA_DIR/bestiary_3/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b3.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-b3.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-b3.db >> $DATA_DIR/urllist.txt.tmp

# NPC Codex
./rules_loader.py      -d $DATA_DIR/book-npc.db               $DATA_DIR/npc_codex/structure.json
./index_loader.py      -d $DATA_DIR/book-npc.db
./url_ref_loader.py    -d $DATA_DIR/book-npc.db               $DATA_DIR/npc_codex/urlref.json
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-npc.db >> $DATA_DIR/urllist.txt.tmp
echo 'select url from sections where url is not null order by url;' | sqlite3 $DATA_DIR/book-npc.db >> $DATA_DIR/supportedurllist.txt.tmp
echo 'select url from url_references where url is not null order by url;' | sqlite3 $DATA_DIR/book-npc.db >> $DATA_DIR/urllist.txt.tmp


# Central Index
./central_index_loader.py   -d $DATA_DIR/index.db   $DATA_DIR/book-*.db
./menu_loader.py            -d $DATA_DIR/index.db   $DATA_DIR/menu.json

# OGL and Community Use License
./rules_loader.py      -d $DATA_DIR/book-ogl.db               $DATA_DIR/ogl/structure.json
./index_loader.py      -d $DATA_DIR/book-ogl.db

cat $DATA_DIR/urllist.txt.tmp | sort > $DATA_DIR/urllist.txt
cat $DATA_DIR/supportedurllist.txt.tmp | sort > $DATA_DIR/supportedurllist.txt
rm $DATA_DIR/urllist.txt.tmp
rm $DATA_DIR/supportedurllist.txt.tmp

