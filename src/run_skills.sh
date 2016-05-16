#!/bin/bash
set -e

source ./dir.conf
./skill_parse.py -o $DATA_DIR -b "Core Rulebook" $WEB_DIR/pathfinderRPG/prd/skills/*.html

