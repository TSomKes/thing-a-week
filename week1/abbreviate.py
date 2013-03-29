#!/usr/bin/env python

import fileinput
import re


def AbbreviateLine(line, threshold):
    """Rebuild the line word by word, abbreviating each word if needed."""
    processed_words = []

    regex = r"\b[a-z]+\b"

    # Find whitespace-delimited "sequences", and see if they contain words long
    # enough to match our criteria.
    # For example, in the string "monkey see, monkey do", one such sequence
    # would be "see,".  We want to isolate the word "see" from the comma before
    # we work on it.
    for sequence in line.split():
        match = re.search(regex, sequence, re.I)

        if match:
            word = match.group(0)
            length = len(word)
            if length >= abbreviation_threshold:
                abbreviated_word = word[0] + str(length - 2) + word[-1]
                sequence = sequence.replace(word, abbreviated_word)

        processed_words.append(sequence)

    return " ".join(processed_words)


abbreviation_threshold = 10

for line in fileinput.input():
    print AbbreviateLine(line, abbreviation_threshold)
