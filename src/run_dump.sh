#!/bin/bash
set -e

source dir.conf

rm -rf $DUMP_DIR/*

./data_unload.py -d $DATA_DIR/book-apg.db -o $DUMP_DIR -b "Advanced Player's Guide"
./data_unload.py -d $DATA_DIR/book-arg.db -o $DUMP_DIR -b "Advanced Race Guide"
./data_unload.py -d $DATA_DIR/book-b1.db -o $DUMP_DIR -b "Bestiary"
./data_unload.py -d $DATA_DIR/book-b2.db -o $DUMP_DIR -b "Bestiary 2"
./data_unload.py -d $DATA_DIR/book-b3.db -o $DUMP_DIR -b "Bestiary 3"
./data_unload.py -d $DATA_DIR/book-b4.db -o $DUMP_DIR -b "Bestiary 4"
./data_unload.py -d $DATA_DIR/book-cr.db -o $DUMP_DIR -b "Core Rulebook"
./data_unload.py -d $DATA_DIR/book-gmg.db -o $DUMP_DIR -b "Game Mastery Guide"
./data_unload.py -d $DATA_DIR/book-ma.db -o $DUMP_DIR -b "Mythic Adventures"
./data_unload.py -d $DATA_DIR/book-uc.db -o $DUMP_DIR -b "Ultimate Combat"
./data_unload.py -d $DATA_DIR/book-ucampaign.db -o $DUMP_DIR -b "Ultimate Campaign"
./data_unload.py -d $DATA_DIR/book-ue.db -o $DUMP_DIR -b "Ultimate Equipment"
./data_unload.py -d $DATA_DIR/book-um.db -o $DUMP_DIR -b "Ultimate Magic"
./data_unload.py -d $DATA_DIR/book-npc.db -o $DUMP_DIR -b "NPC Codex"
./data_unload.py -d $DATA_DIR/book-mc.db -o $DUMP_DIR -b "Monster Codex"
./data_unload.py -d $DATA_DIR/book-tech.db -o $DUMP_DIR -b "Technology Guide"
