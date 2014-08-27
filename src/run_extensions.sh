#!/bin/bash
set -e

source dir.conf
./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-cr.db -b "Core Rulebook" 
./extension_loader.py -d ../../pfsrd-data/book-cr.db ../../pfsrd-data/core_rulebook/extensions/items.json

./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-apg.db -b "Advanced Player's Guide"
./extension_loader.py -d ../../pfsrd-data/book-apg.db ../../pfsrd-data/advanced_players_guide/extensions/items.json

./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-arg.db -b "Advanced Race Guide"
./extension_loader.py -d ../../pfsrd-data/book-arg.db ../../pfsrd-data/advanced_race_guide/extensions/items.json

./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-uc.db -b "Ultimate Combat"
./extension_loader.py -d ../../pfsrd-data/book-uc.db ../../pfsrd-data/ultimate_combat/extensions/items.json

./item_table_dump.py -o $DATA_DIR -d $DATA_DIR/book-ue.db -b "Ultimate Equipment"
./extension_loader.py -d ../../pfsrd-data/book-ue.db ../../pfsrd-data/ultimate_equipment/extensions/items.json

