#!/usr/bin/env bash

CODE_DIR=~/code/

# Find all project directories immediately under code folder
find $CODE_DIR -maxdepth 1 -mindepth 1 -type d
