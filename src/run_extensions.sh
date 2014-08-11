#!/bin/bash
set -e

source dir.conf
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-cr.db -b "Core Rulebook" 
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-apg.db -b "Advanced Player's Guide"
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-arg.db -b "Advanced Race Guide"
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-uc.db -b "Ultimate Combat"
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-ue.db -b "Ultimate Equipment"
