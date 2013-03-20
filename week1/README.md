Thing-a-Week, Week 1:  Abbreviation & Debreviation, i18n-Style
========

Overview
--------
Some coworkers & I used to get a chuckle out of the "internationalization" = "i18n", "localization" = "L10n" abbreviation scheme.  

The fun part of this abbreviation is that it's so [lossy](http://en.wikipedia.org/wiki/Lossy).  (The string "i18n" is only useful for people already familiar with the concept of internationalization, or at least the term.)

In an effort to automate the fun away, I've decided to make a quick script that dehydrates & rehydrates a given string using this form of compression.

(NB:  This form of abbreviation apparently falls under the umbrella term [numeronym](http://en.wikipedia.org/wiki/Numeronym), which seems unfortunate.  None of the other phenomena in that article appear to be functionally similar.)

Things I learned while doing this
---------------------------------
I didn't know about fileinput, which I learned about here:  http://stackoverflow.com/a/1454400/18347.  

Using this gives us "expected" Unix-y behavior:  you can pass in standard input, or you can pass a filename in as an argument.  In other words, either of these work:

    $ python ./abbreviate.py README.md
	 $ cat README | python ./abbreviate.py
