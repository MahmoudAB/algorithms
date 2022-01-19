# // --- Directions
# // Write a function that returns the number of vowels
# // used in a string.  Vowels are the characters 'a', 'e'
# // 'i', 'o', and 'u'.
# // --- Examples
# //   vowels('Hi There!') --> 3
# //   vowels('Why do you ask?') --> 4
# //   vowels('Why?') --> 0

import unittest


def vowels(string):
    count = 0
    for i in string.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


class VowelsTest(unittest.TestCase):

    def test_returns_number_of_vowels(self):
        self.assertEqual(vowels("aeiou"), 5)

    def test_returns_number_of_vowels_when_capitalized(self):
        self.assertEqual(vowels("AEIOU"), 5)

    def test_returns_number_of_vowels_2(self):
        self.assertEqual(vowels("abcdefghijklmnopqrstuvwxyz"), 5)

    def test_returns_number_of_vowels_3(self):
        self.assertEqual(vowels("bcdfghjkl"), 0)
