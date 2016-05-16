#!/bin/bash
set -e

source ./dir.conf
mkdir -p $DATA_DIR
rm -rf $DATA_DIR/*

cp -r ../structure/* $DATA_DIR

./run_classes.sh
./run_feats.sh
./run_races.sh
./run_rules.sh
./run_skills.sh
./run_spell_lists.sh
./run_spells.sh
./run_creatures.sh
