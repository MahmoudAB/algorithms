# // --- Directions
# // Check to see if two provided strings are anagrams of eachother.
# // One string is an anagram of another if it uses the same characters
# // in the same quantity. Only consider characters, not spaces
# // or punctuation.  Consider capital letters to be the same as lower case
# // --- Examples
# //   anagrams('rail safety', 'fairy tales') --> True
# //   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
# //   anagrams('Hi there', 'Bye there') --> False

import unittest


def anagrams(str1, str2):
    return create_map(get_alpha_chars(str1)) == create_map(get_alpha_chars(str2))


def get_alpha_chars(string):
    alphas = ""
    for i in string:
        if i.isalpha():
            alphas += i
    return alphas.lower()


def create_map(a_str):
    a_map = {}
    for i in a_str:
        if i in a_map:
            a_map[i] += 1
        else:
            a_map[i] = 1
    return a_map


class AnagramsTest(unittest.TestCase):

    def test_hello(self):
        self.assertTrue(anagrams('hello', 'llohe'))

    def test_hi(self):
        self.assertTrue(anagrams('Whoa! Hi!', 'Hi! Whoa!'))

    def test_two(self):
        self.assertFalse(anagrams('One One', 'Two two two'))

    def test_one(self):
        self.assertFalse(anagrams('One one', 'One one c'))

    def test_tree(self):
        self.assertFalse(anagrams('A tree, a life, a bench', 'A tree, a fence, a yard'))
