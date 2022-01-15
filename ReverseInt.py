import unittest


# // --- Directions
# // Given an integer, return an integer that is the reverse
# // ordering of numbers.
# // --- Examples
# //   reverseInt(15) === 51
# //   reverseInt(981) === 189
# //   reverseInt(500) === 5
# //   reverseInt(-15) === -51
# //   reverseInt(-90) === -9


def reverseInt(number):
    reversed = ""
    if number >= 0:
        reversed = reverse(number, reversed)
    else:
        reversed = "-" + reverse(number * -1, reversed)
    return int(reversed)


def reverse(number, reversed):
    for i in range(len(str(number))):
        reversed = str(number)[i] + reversed
    return reversed


class ReverseIntTest(unittest.TestCase):

    def test(self):
        self.assertEqual(reverseInt(0), 0)

    def testReversePositiveNumbers(self):
        self.assertEqual(reverseInt(5), 5)
        self.assertEqual(reverseInt(15), 51)
        self.assertEqual(reverseInt(90), 9)
        self.assertEqual(reverseInt(2359), 9532)

    def testReverseNegativeNumbers(self):
        self.assertEqual(reverseInt(-5), -5)
        self.assertEqual(reverseInt(-15), -51)
        self.assertEqual(reverseInt(-90), -9)
        self.assertEqual(reverseInt(-2359), -9532)


if __name__ == "__main__":
    tests = ReverseIntTest()
    tests.testReversePositiveNumbers()
    tests.testReverseNegativeNumbers()
    tests.test()
