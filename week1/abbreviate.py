#!/usr/bin/env python

import fileinput
import re


def A8e(line, threshold=10):
    """Return a string with long words abbreviated i18n-style."""

    # Find all words with at least [threshold] sequential letters
    regex = r"\b[a-z]{%d,}\b" % threshold

    longWords = re.findall(regex, line, re.IGNORECASE)

    for word in longWords:
        innerLength = len(word) - 2
        abbreviatedWord = word[0] + str(innerLength) + word[-1]
        line = line.replace(word, abbreviatedWord)

    return line


for line in fileinput.input():
    print A8e(line),
