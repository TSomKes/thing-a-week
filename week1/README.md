Thing-a-Week, Week 1:  Abbreviation, i18n-Style
========

Overview
--------
Some coworkers & I used to get a chuckle out of the "internationalization" =
"i18n", "localization" = "L10n" abbreviation scheme.  

The fun part of this abbreviation is that it's so
[lossy](http://en.wikipedia.org/wiki/Lossy).  (The string "i18n" is only useful
for people already familiar with the concept of internationalization, or at
least the term.)

In an effort to automate the fun away, I've decided to make a quick script that
dehydrates a given string using this form of compression.

(NB:  This form of abbreviation apparently falls under the umbrella term
[numeronym](http://en.wikipedia.org/wiki/Numeronym), which seems unfortunate.
None of the other phenomena in that article appear to be functionally similar.)

Also:  Thank you, Project Gutenberg, for all of my test literature.
Specifically, the text of the Declaration of Independence that I used came from
here:  http://www.gutenberg.org/files/16780/16780-0.txt.

Example
-------
Running part of the Declaration of Independence through this code, with an
abbreviation threshold of eight (meaning word eight characters or longer will
be abbreviated), turns this:

> The unanimous Declaration of the thirteen united States of America

into this:

> The u7s D9n of the t6n united States of America

If we drop the threshold to five, we get this:

> The u7s D9n of the t6n u4d S4s of A5a

Things I learned while doing this
---------------------------------
### fileinput ###
I didn't know about fileinput, which I learned about here:
http://stackoverflow.com/a/1454400/18347.  

Using this gives us "expected" Unix-y behavior:  you can pass in standard
input, or you can pass a filename in as an argument.  In other words, either of
these work:

    $ ./abbreviate.py README.md
    $ cat README | ./abbreviate.py

### Regex vs. iterating-over-characters ###
Initially, I worried that I might be introducing too much overhead with the
regex approach to finding candidate words for abbreviation.  I tried
implementing a character-by-character iteration of the line instead, which
would identify words by isalpha() checks on the individual characters.  If the
words were long enough, they'd be abbreviated as they were added to the
processed string.

This seems to have been a bit faster for shorter input strings, and quite a
bit slower for longer input strings.  I don't know if this is the case, but I
wonder if the regex overhead is too much for tiny inputs, but that the
efficiency overtakes the overhead for longer inputs.

This is all wild guessing, though.

### Regex findall()  ###
I think my early attempts to roll my own way of iterating over the string
looking for regex hits was misguided.  It ended up being harder to understand,
and (I suspect) less Python-idiomatic ("Pythonic") than later approaches.

I'm not convinced that I've landed on the optimal solution, but it's good
enough for now.
