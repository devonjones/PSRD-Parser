#!/bin/bash
find ../local/ -name "*.json" | xargs ./json_loader.py -d ../local/psrd.db

