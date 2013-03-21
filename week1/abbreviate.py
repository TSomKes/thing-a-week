import fileinput
import re


def AbbreviateLine(line, threshold):
    # We'll rebuild our abbreviated line word by word, checking each word to
    # see if it needs to be abbreviated.
    processed_words = []

    # Find whitespace-delimited "sequences", and see if they contain words long
    # enough to match our criteria.  For example, in the string "monkey see,
    # monkey do", one such sequence would be "see,".  We want to isolate the 
    # word "see" from the comma before we work on it.
    for sequence in line.split():
        match = word_pattern.search(sequence)

        if match:
            word = match.group(0)
            length = len(word)
            if length >= abbreviation_threshold:
                abbreviated_word = word[0] + str(length - 2) + word[-1]
                sequence = sequence.replace(word, abbreviated_word)

        processed_words.append(sequence)

    # We're eliminating all the whitspace, so we need to re-add our own newline
    return " ".join(processed_words) + '\r\n'


# We'll be using this regex a lot; compile it here.
word_pattern = re.compile(r"\b[a-z]+\b", re.I)

abbreviation_threshold = 10

processed_lines = []

for line in fileinput.input():
    processed_lines.append(AbbreviateLine(line, abbreviation_threshold))

output = "".join(processed_lines)

print output
