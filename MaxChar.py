# // --- Directions
# // Given a string, return the character that is most
# // commonly used in the string.
# // --- Examples
# // maxChar("abcccccccd") === "c"
# // maxChar("apple 1231111") === "1"

import unittest


# map method
def maxchar(str):
    chars = {}
    maximum = 0
    maxChar = ''
    for i in range(len(str)):
        if str[i] not in chars:
            chars[str[i]] = 1
        else:
            chars[str[i]] += 1

    for char in chars:
        if chars[char] > maximum:
            maximum = chars[char]
            maxChar = char

    return maxChar


class MaxChar(unittest.TestCase):
    def test(self):
        self.assertEqual(maxchar("a"), "a")
        self.assertEqual(maxchar("abcdefghijklmnaaaaa"), "a")
        self.assertEqual(maxchar("ab1c1d1e1f1g1"), "1")
        self.assertEqual(maxchar("apple 1231111"), "1")

# brut force method
# def maxchar(str):
#     maximum = ''
#     count = 0
#     max_count = 0
#     for i in range(len(str)):
#         for j in range(len(str)):
#             if str[i] == str[j]:
#                 count = count + 1
#             if count > max_count:
#                 maximum = str[i]
#     return maximum
