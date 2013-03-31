Thing-a-Week, Week 2:  Debreviation, i18n-Style
========

Overview
--------
Part II of the "i18n abbreviation/debreviation" project from [Week 1](../week1).

I admit it:  "debreviate" is a made-up word, though I'm apparently not the
first to make it up.  

This is intended to be an inaccurate, and hopefully humorous, process.

Example
-------
Using the example from the [Week 1 readme](../week1/README.md),

> The u7s D9n of the t6n united States of America

this script produces the following:

> The underacts Destination of the terrapin united States of America

At least, it did this time.  Next run, it'll probably come up with different words.

Also, for my taste, it's funnier when the threshold is a little higher:  better
to keep most of the high-flown language intact, so that the odd words are more
unexpected.

For example, with a threshold as low as five we get the following:

> The undresses Desecration of the traction unfold Slinks of Ammonia

Tiresome?  You decide.

Things I learned while doing this
---------------------------------
Hoo, boy.  Lots, but hard to think of particularly big things:  I think I still
remember a lot of lessons from last week.  Almost like I'm retaining
information!

One thing I haven't learned:  how to name variables & functions.  Boy, do those
things need fixin'.

Notes
-----
I'm not terribly happy with the way this searches the word file for matching
words.  Walking the file once per pattern we're trying to match feels
inefficient.  On the other hand, walking the file once and comparing against
each of the patterns also sounds inefficient.  (I suppose I should set both up
& time them sometime.)
