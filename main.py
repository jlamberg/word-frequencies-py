# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

def get_input_text(filename):
    with open(filename) as f:
        text = f.read()
    return text

def split_to_words(text):
    words = text.split()
    return words

def calculate_frequencies(words):
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def output_frequencies(frequencies):
    for word, frequency in frequencies.items():
        print(word, frequency)

def main(filename):
    text = get_input_text(filename)
    words = split_to_words(text)
    frequencies = calculate_frequencies(words)
    output_frequencies(frequencies)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % (sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])
