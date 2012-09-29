#!/bin/bash
set -e

dir=$(cd $(dirname $0); pwd)
source $dir/dir.conf

$dir/creature_dump.py -d $DATA_DIR/psrd.db Ghoul
