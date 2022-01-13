import unittest


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
