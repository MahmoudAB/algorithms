# // --- Directions
# // Write a function that accepts a positive number N.
# // The function should console log a pyramid shape
# // with N levels using the # character.  Make sure the
# // pyramid has spaces on both the left *and* right hand sides
# // --- Examples
# //   pyramid(1)
# //       '#'
# //   pyramid(2)
# //       ' # '
# //       '###'
# //   pyramid(3)
# //       '  #  '
# //       ' ### '
# //       '#####'
import math


def pyramid(n, row=0, level=''):
    if n == row:
        return
    if len(level) == 2*n-1:
        print(level)
        return pyramid(n, row+1)

    midpoint = math.floor((2*n-1)/2)
    add = ""
    if midpoint - row <= len(level) <= midpoint + row:
        add = "#"
    else:
        add = " "
    pyramid(n, row, level+add)



pyramid(2)
print("another one")
pyramid(3)
print("another one")
pyramid(5)