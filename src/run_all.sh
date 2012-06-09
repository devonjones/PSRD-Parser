#!/bin/bash
source dir.conf
mkdir -p $DATA_DIR
rm -rf $DATA_DIR/*

cp -r ../structure/* $DATA_DIR

./local_classes.sh
./local_feats.sh
./local_races.sh
./local_rules.sh
./local_skills.sh
./local_spell_lists.sh
./local_spells.sh
./local_creatures.sh
