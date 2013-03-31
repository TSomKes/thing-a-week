#!/usr/bin/env python

import fileinput
import re


def GetAbbreviations(line):
    """Return a list of all i18n-style abbreviations in the given string."""

    # Find strings with: single letter, 1+ numbers, single letter
    regex = r"\b[a-z][0-9]+[a-z]\b"

    return re.findall(regex, line, re.IGNORECASE)


def GetMatchingWords(abbreviations):
    """
    Return a dictionary of lists of words matching the given abbreviations

    abbreviations - List of abbreviations to be matched against word list
    (Note:  May contain duplicates, which will be removed during processing.)

    Returned dictionary will be of the shape
    { 'c2t' : ['cart', 'coat', 'colt'], 'f4d' : ['faired', 'feared']}
    """
    matchDict = {}

    with open("/usr/share/dict/words") as wordFile:
        for abb in abbreviations:
            if abb not in matchDict.keys():
                missingLetterCount = int(abb[1:-1])
                pattern = '^%s[a-z]{%d}%s$' % (abb[0], missingLetterCount, abb[-1])

                wordFile.seek(0)
                words = []
                for line in wordFile:
                    match = re.match(pattern, line, re.IGNORECASE)
                    if match:
                        words.append(match.group(0))
                matchDict[abb] = words

    return matchDict


lines = []

# Make a local copy of the lines
for line in fileinput.input():
    lines.append(line)


abbreviations = []

for line in lines:
    abbreviationsNew = GetAbbreviations(line)
    if abbreviationsNew:
        abbreviations.extend(abbreviationsNew)

abbreviations.sort()

matchingWords = GetMatchingWords(abbreviations)

print matchingWords
