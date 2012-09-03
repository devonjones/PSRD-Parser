#!/bin/bash
set -e

source dir.conf
./race_parse.py -o $DATA_DIR -b "Core Rulebook" $WEB_DIR/pathfinderRPG/prd/races.html 

./arg_race_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "core"     $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/coreRaces/*.html
./arg_race_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "featured" $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/featuredRaces/*.html
./arg_race_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "uncommon" $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/uncommonRaces/*.html
