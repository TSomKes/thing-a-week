#!/usr/bin/env bash

# Determines which projects, if any, have locally-committed changes that have
# not yet been pushed to their repo-in-the-cloud.
#
# How?  Walk the project directories, determine which DVCS is being used for
# each, and see if any local changes haven't been pushed yet.

code_dir=~/code/

# Find all project directories immediately under code folder
for dir in `find $code_dir -maxdepth 1 -mindepth 1 -type d | sort`
do
	# Move into $dir, in case we find a repo, so that the git/hg commands work
	# relative to the working directory
	cd $dir

	project=${PWD##*/}

	# .git directory found?  Git repo.
	if [ -d $dir"/.git" ]; then
		dvcs="Git"
		dvcs_output=$(git push --dry-run 2>&1) # Git puts our message on stderr
		syncd_message="Everything up-to-date"

	# .hg directory found?  Hg repo.
	elif [ -d $dir"/.hg" ]; then
		dvcs="Hg"
		dvcs_output=$(hg outgoing)
		syncd_message="no changes found"

	else
		dvcs="no repo found"
		dvcs_output=""
		syncd_message="not applicable"
	fi

	# If dvcs_output contains syncd_message, local repo has no un-pushed commits
	if [[ "$dvcs_output" == *"$syncd_message"* ]]; then
		status="sync'd"
	else 
		status="un-pushed local commits found"
	fi

	echo $project" - "$dvcs" - "$status

	# Move back to the original directory, just 'cause.
	cd $code_dir
done
