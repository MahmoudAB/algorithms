# // --- Directions
# // Write a function that accepts an integer N
# // and returns a NxN spiral matrix.
# // --- Examples
# //   matrix(2)
# //     [[1, 2],
# //     [4, 3]]
# //   matrix(3)
# //     [[1, 2, 3],
# //     [8, 9, 4],
# //     [7, 6, 5]]
# //  matrix(4)
# //     [[1,   2,  3, 4],
# //     [12, 13, 14, 5],
# //     [11, 16, 15, 6],
# //     [10,  9,  8, 7]]

import unittest


def matrix(n):
    result = [[0 for i in range(n)] for j in range(n)]
    counter = 1
    start_column = 0
    end_column = n - 1
    start_row = 0
    end_row = n - 1
    while start_column <= end_column and start_row <= end_row:
        # top row
        for i in range(start_column, end_column + 1):
            result[start_row][i] = counter
            counter += 1

        start_row += 1

        # right column
        for i in range(start_row, end_row + 1):
            result[i][end_column] = counter
            counter += 1

        end_column -= 1

        # Bottom row
        for i in range(end_column + 1, start_column, -1):
            result[end_row][i - 1] = counter
            counter += 1

        end_row -= 1

        # start column
        for i in range(end_row + 1, start_row, -1):
            result[i - 1][start_column] = counter
            counter += 1

        start_column += 1
    return result


class MatrixClass(unittest.TestCase):

    def test_produces_2x2_array(self):
        m = matrix(2)
        self.assertEqual(m[0], [1, 2])
        self.assertEqual(m[1], [4, 3])

    def test_produces_3x3_array(self):
        m = matrix(3)
        self.assertEqual(m[0], [1, 2, 3])
        self.assertEqual(m[1], [8, 9, 4])
        self.assertEqual(m[2], [7, 6, 5])

    def test_produces_4x5_array(self):
        m = matrix(4)
        self.assertEqual(m[0], [1, 2, 3, 4])
        self.assertEqual(m[1], [12, 13, 14, 5])
        self.assertEqual(m[2], [11, 16, 15, 6])
        self.assertEqual(m[3], [10, 9, 8, 7])
