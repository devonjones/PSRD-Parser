#!/bin/bash

source dir.conf
rm $DATA_DIR/index.db
set -e
cp -r ../structure/* $DATA_DIR

# Central Index
./central_index_loader.py   -d $DATA_DIR/index.db   $DATA_DIR/book-*.db
./menu_loader.py            -d $DATA_DIR/index.db   $DATA_DIR/menu.json
