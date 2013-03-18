Some coworkers & I used to get a chuckle out of the i18n == "internationalization" abbreviation scheme.  I've seen the same done for "localization" (L10n).  

This form of abbreviation apparently falls under the umbrella term [numeronym](http://en.wikipedia.org/wiki/Numeronym), which seems unfortunate.  (None of the other phenomena in that article appear to be functionally similar.)

The fun part of this abbreviation is that it's so [lossy](http://en.wikipedia.org/wiki/Lossy).  (The string "i18n" is only useful for people already familiar with the concept of internationalization, or at least the term.)

In an effort to automate the fun away, I've decided to make a quick script that dehydrates & rehydrates a given string using this form of compression.
