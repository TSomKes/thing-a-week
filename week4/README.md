Thing-a-Week, Week 4:  Multi-project, multi-DVCS status script
==============================================================

Overview
--------
I've got a lot of projects in flight at once.  Or idling on the runway, or
rotting in the plane graveyard, or whatever.

On my machine, they're all hosted in directories under ~/code/, though they all
come from repos on either GitHub or BitBucket.  Some are Git repos, some are
Hg.

I often work offline, and I often work in short bursts on different projects.
Sometimes I forget which projects have local changes that haven't been pushed
back to the cloud.

I figured I should try to put together a little script to help me with that.

Example
-------
```
$ ./repo_push_status.bash
arcade - Git - sync'd
beaker - Git - un-pushed local commits found
dotfiles - Git - sync'd
homework - Git - sync'd
journal - Hg - sync'd
orangutan - Git - sync'd
rando - Hg - sync'd
sketchbook - Git - sync'd
thing-a-week - Git - un-pushed local commits found
tsomkes.com - Hg - un-pushed local commits found
```

Things I learned while doing this
---------------------------------
My Bash Fu is very weak, and I was afraid finding all the project directories
under code/ was going to be very difficult.  Turns out find made it super-easy:
http://stackoverflow.com/questions/2107945/how-to-loop-over-directories-in-linux.

...holy crap, I don't know what I'm doing here.  Bash is a tangled mess.  My
script works, but I imagine it's littered with efficiency issues,
quote-escaping issues, etc.

I have no idea if I'm doing the string concatenation for the path-building
correctly, but it seems to be working.  

Why on earth does Git send its "Everything up-to-date" message to stderr?  I
chased problems with that for many, many minutes, all the time assuming my
stdout-to-variable technique was wrong.  Well, it might still be wrong, but it
works.

Thanks to
http://stackoverflow.com/questions/1371261/get-current-directory-name-without-full-path-in-bash-script,
I was able to get the project name out of the current working directory.  (Some
day, I need to learn how/why this works, this parameter expansion thing...)
