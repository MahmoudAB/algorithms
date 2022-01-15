import unittest

# // --- Directions
# // Given a string, return true if the string is a palindrome
# // or false if it is not.  Palindromes are strings that
# // form the same word if it is reversed. *Do* include spaces
# // and punctuation in determining if the string is a palindrome.
# // --- Examples:
# //   palindrome("abba") === true
# //   palindrome("abcdefg") === false

def palindrome(str):
    reversed = ""
    for i in range(len(str)):
        reversed = str[i] + reversed
    return reversed == str


class PalindromeTest(unittest.TestCase):

    def tests(self):
        self.assertTrue(palindrome("aba"))
        self.assertTrue(palindrome("1000000001"))
        self.assertTrue(palindrome("pennep"))
        self.assertFalse(palindrome(" aba"))
        self.assertFalse(palindrome("aba "))
        self.assertFalse(palindrome("greetings"))
        self.assertFalse(palindrome("Fish hsif"))

        if __name__ == "__main__":
            self.tests()
