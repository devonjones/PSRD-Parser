#!/bin/bash
mkdir -p ../local
rm -rf ../local/*

cp -r ../structure/* ../local

./local_classes.sh
./local_feats.sh
./local_races.sh
./local_rules.sh
./local_skills.sh
./local_spell_lists.sh
./local_spells.sh
