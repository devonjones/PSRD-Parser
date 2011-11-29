#!/bin/bash
mkdir -p ../data
rm -rf ../data/*

./run_classes.sh
./run_feats.sh
./run_races.sh
./run_rules.sh
./run_skills.sh
./run_spell_lists.sh
./run_spells.sh
