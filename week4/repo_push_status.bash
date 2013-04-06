#!/usr/bin/env bash

CODE_DIR=~/code/

# Find all project directories immediately under code folder
for dir in `find $CODE_DIR -maxdepth 1 -mindepth 1 -type d`
do
	if [ -d $dir"/.git" ]; then
		echo $dir "- Git"
	elif [ -d $dir"/.hg" ]; then
		echo $dir "- Hg"
	else
		echo $dir "- no repo found"
	fi
done
