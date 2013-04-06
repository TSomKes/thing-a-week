#!/usr/bin/env bash

# Determines which projects, if any, have locally-committed changes that have
# not yet been pushed to their repo-in-the-cloud.
#
# How?  Walk the project directories, determine which DVCS is being used for
# each, and see if any local changes haven't been pushed yet.

code_dir=~/code/

git_syncd_message="Everything up-to-date"
hg_syncd_message="no changes found"

# Find all project directories immediately under code folder
for dir in `find $code_dir -maxdepth 1 -mindepth 1 -type d`
do
	# Move into $dir, in case we find a repo, so that the git/hg commands work
	# relative to the working directory
	cd $dir

	status=$dir

	# .git directory found?  Git repo.
	if [ -d $dir"/.git" ]; then

		status+="- Git - "

		git_output=$(git push --dry-run 2>&1)
		if [[ "$git_output" == *"$git_syncd_message"* ]]; then
			status+="sync'd"
		else 
			status+="un-sync'd local changes found"
		fi

	# .hg directory found?  Hg repo.
	elif [ -d $dir"/.hg" ]; then

		status+="- Hg - "

		hg_output=$(hg outgoing)
		if [[ "$hg_output" == *"$hg_syncd_message"* ]]; then
			status+="sync'd"
		else 
			status+="un-sync'd local changes found"
		fi

	else
		status+="- no repo found"
	fi

	echo $status

	# Move back to the original directory, just 'cause.
	cd $code_dir
done
