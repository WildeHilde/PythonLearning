"""With this string:
'monty pythons flying circus'

Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'

Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']

Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

Created on 3 Nov 2015

@author: paulross
"""
import pytest

def no_duplicates(a_string):

    res = ""
    alph = "abcdefghijklmnopqrstuvwxyz "

    for i in range(0, len(a_string)):
        if ((a_string[i] in alph) and a_string[i] not in res):
            res += a_string[i]

    return "".join(sorted(res))

def reversed_words(a_string):
    return a_string.split(" ")[::-1]


def four_char_strings(a_string):
    res = []

    for i in range(0, len(a_string)):
        if i%4 == 0:
            res.append(a_string[i:(i+4)])

    return res


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
