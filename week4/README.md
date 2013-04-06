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
At the moment:

```
$ ./repo_push_status.bash
/home/tsomkes/code/homework - Git
/home/tsomkes/code/tsomkes.com - Hg
/home/tsomkes/code/rando - Hg
/home/tsomkes/code/journal - Hg
/home/tsomkes/code/sketchbook - Git
/home/tsomkes/code/beaker - Git
/home/tsomkes/code/arcade - Git
/home/tsomkes/code/thing-a-week - Git
/home/tsomkes/code/orangutan - Git
/home/tsomkes/code/dotfiles - Git
```

Things I learned while doing this
---------------------------------
My Bash Fu is very weak, and I was afraid finding all the project directories
under code/ was going to be very difficult.  Turns out find made it super-easy:
http://stackoverflow.com/questions/2107945/how-to-loop-over-directories-in-linux.

I have no idea if I'm doing the string concatenation for the path-building
correctly, but it seems to be working.  
