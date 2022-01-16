# // --- Directions
# // Given an array and chunk size, divide the array into many subarrays
# // where each subarray is of length size
# // --- Examples
# // chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# // chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# // chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# // chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# // chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

import unittest


def chunk(array, size):
    chunked = []
    last = []

    for element in array:
        if not last:
            last.append(element)
            chunked.append(last)
        elif len(last) == size:
            last = [element]
            chunked.append(last)
        else:
            last.append(element)
    return chunked


class ChunkTest(unittest.TestCase):

    def test_10elements_size2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chunked = chunk(arr, 2)
        self.assertEqual(chunked, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

    def test_3elements_size1(self):
        arr = [1, 2, 3]
        chunked = chunk(arr, 1)
        self.assertEqual(chunked, [[1], [2], [3]])

    def test_5elements_size3(self):
        arr = [1, 2, 3, 4, 5]
        chunked = chunk(arr, 3)
        self.assertEqual(chunked, [[1, 2, 3], [4, 5]])

    def test_13elements_size5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        chunked = chunk(arr, 5)
        self.assertEqual(chunked, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]])
