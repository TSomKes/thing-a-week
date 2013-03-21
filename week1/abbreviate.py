import fileinput
import re

# We'll be using this regex a lot; compile it here.
word_pattern = re.compile(r"\b[a-z]+\b", re.I)

abbreviation_threshold = 10

processed_lines = []

for line in fileinput.input():
    # We'll rebuild our abbreviated line word by word, checking each word to see
    # if it needs to be abbreviated.
    processed_words = []

    # Find whitespace-delimited "sequences", and see if they contain words long
    # enough to match our criteria.  For example, in the string "I think,
    # therefore I am", one such sequence would be "think,".  We want to isolate
    # the word "think" from the comma before we work on it.
    for sequence in line.split():
        match = word_pattern.search(sequence)

        if match:
            word = match.group(0)
            length = len(word)
            if length >= abbreviation_threshold:
                abbreviated_word = word[0] + str(length - 2) + word[-1]
                sequence = sequence.replace(word, abbreviated_word)

        processed_words.append(sequence)

    processed_lines.append(" ".join(processed_words))

output = "\n".join(processed_lines)

print output
