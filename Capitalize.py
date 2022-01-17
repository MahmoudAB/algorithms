# // --- Directions
# // Write a function that accepts a string.  The function should
# // capitalize the first letter of each word in the string then
# // return the capitalized string.
# // --- Examples
# //   capitalize('a short sentence') --> 'A Short Sentence'
# //   capitalize('a lazy fox') --> 'A Lazy Fox'
# //   capitalize('look, it is working!') --> 'Look, It Is Working!'

import unittest


def capitalize(string):
    result = string[0].capitalize()
    for i in range(1, len(string)):
        if string[i-1] == " ":
            result += string[i].capitalize()
        else:
            result += string[i]
    return result


class CapitalizeTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(capitalize("hi there, how is it going?"), "Hi There, How Is It Going?")

    def test_2(self):
        self.assertEqual(capitalize("i love breakfast at bill miller bbq"), "I Love Breakfast At Bill Miller Bbq")

    def test_extra(self):
        self.assertEqual(capitalize("hi"), "Hi")
