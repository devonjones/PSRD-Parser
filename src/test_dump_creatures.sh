#!/bin/bash
set -e

dir=$(cd $(dirname $0); pwd)
source $dir/dir.conf

$dir/test_creature_dump.py
