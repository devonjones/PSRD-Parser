#!/bin/bash
./feat_load.py -d ../local/psrd.db ../local/core_rulebook/feats/*.json
./feat_load.py -d ../local/psrd.db ../local/bestiary/feats/*.json
./feat_load.py -d ../local/psrd.db ../local/advanced_players_guide/feats/*.json
./feat_load.py -d ../local/psrd.db ../local/ultimate_magic/feats/*.json
./feat_load.py -d ../local/psrd.db ../local/ultimate_combat/feats/*.json

