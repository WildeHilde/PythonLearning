#!/usr/bin/env python
"""Created by Jannik Carl"""

import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

FILENAME = r"C:\Users\Jannik\OneDrive\Programmieren\Python\Training\fairytale.txt"
text = "aabbccceeffase"

def load_text(filename):
    """Load the text from a file"""
    tmp = open("{0}".format(filename))
    return ' '.join(tmp.readlines())

def count_letter(txt, l):
    """Count how many times the letter appears in the text"""
    amount = re.findall(r"{0}".format(l), txt, re.IGNORECASE)
    return len(amount)

def create_dict(txt):
    """LALALA"""    
    histo = {}
    for c in ALPHABET:
        histo[c] = count_letter(txt, c)
    return histo

def draw_stats(amounts):
    """Creates a visual aid from a dictionary"""
    overall_letters = sum(amounts.values())
    for l, a in amounts.items():
        tmp = (a / overall_letters)*100
        print("{0}: {1}".format(l, round(tmp)*"+"))

def main():
    text = load_text(FILENAME)
    print(create_dict(text))
    draw_stats(create_dict(text))

if __name__ == '__main__':
    main()
