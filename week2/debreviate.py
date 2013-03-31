#!/usr/bin/env python

import fileinput
import random
import re


def GetAbbreviations(line):
    """Return a list of all i18n-style abbreviations in the given string."""

    # Find strings with: single letter, 1+ numbers, single letter
    pattern = r"\b[a-z][0-9]+[a-z]\b"

    return re.findall(pattern, line, re.IGNORECASE)


def GetAbbreviationRegexPattern(abb):
    """Return regex pattern string matching abbreviation."""

    # "i18n" --> 18
    missingLetterCount = int(abb[1:-1])

    # "i18n" --> "^i[a-z]{18}n$"
    return "^%s[a-z]{%d}%s$" % (abb[0], missingLetterCount, abb[-1])


def GetMatchesFromWordFile(pattern):
    """Return list of matched words from word file."""

    with open("/usr/share/dict/words") as wordFile:
        words = []
        for line in wordFile:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                words.append(match.group(0))

    return words


def GetMatchingWords(abbreviations):
    """
    Return a dictionary of lists of words matching the given abbreviations

    abbreviations - List of abbreviations to be matched against word list
    (Note:  May contain duplicates, which will be removed during processing.)

    Returned dictionary will be of the shape
    { 'c2t' : ['cart', 'coat', 'colt'], 'f4d' : ['faired', 'feared'] }
    """
    matchDict = {}

    for abb in abbreviations:
        if abb not in matchDict.keys():
            pattern = GetAbbreviationRegexPattern(abb)
            matchDict[abb] = GetMatchesFromWordFile(pattern)

    return matchDict


def DebreviateLine(line, matchedWords):
    """Replace all abbreviations in given line with words from matchedWords. """
    abbreviatedWords = GetAbbreviations(line)
    for abb in abbreviatedWords:
        matchedWord = random.choice(matchingWords[abb])

        # Keep the first letter of the abbreviation to preserve its case
        newWord = abb[0] + matchedWord[1:]
        
        line = line.replace(abb, newWord, 1)

    return line


lines = []

# Make a local copy of the lines
for line in fileinput.input():
    lines.append(line)

abbreviations = []

for line in lines:
    abbreviations.extend(GetAbbreviations(line))

matchingWords = GetMatchingWords(abbreviations)

for line in lines:
    print DebreviateLine(line, matchingWords),
