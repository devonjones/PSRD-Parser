#!/bin/bash
./json_loader.py -d ../local/psrd.db -p "Races" ../local/*/races/*.json
./json_loader.py -d ../local/psrd.db -p "Classes" ../local/*/classes/*.json
./json_loader.py -d ../local/psrd.db -p "Skills" ../local/*/skills/*.json
./json_loader.py -d ../local/psrd.db -p "Feats" ../local/*/feats/*.json
./json_loader.py -d ../local/psrd.db -p "Spells" ../local/*/spells/*.json
./json_loader.py -d ../local/psrd.db -p "Rules" ../local/*/rules/*.json

