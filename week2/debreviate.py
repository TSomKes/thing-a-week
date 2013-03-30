#!/usr/bin/env python

import fileinput
import re


def GetAbbreviations(line):
    """Return a list of all i18n-style abbreviations in the given string."""

    # Find strings with: single letter, 1+ numbers, single letter
    regex = r"\b[a-z][0-9]+[a-z]\b"

    return re.findall(regex, line, re.IGNORECASE)


lines = []

# Make a local copy of the lines
for line in fileinput.input():
    lines.append(line)


abbreviations = []

for line in lines:
    abbreviationsNew = GetAbbreviations(line)
    if abbreviationsNew:
        abbreviations.extend(abbreviationsNew)

print abbreviations
