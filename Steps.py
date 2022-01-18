# // --- Directions
# // Write a function that accepts a positive number N.
# // The function should console log a step shape
# // with N levels using the # character.  Make sure the
# // step has spaces on the right hand side!
# // --- Examples
# //   steps(2)
# //       '# '
# //       '##'
# //   steps(3)
# //       '#  '
# //       '## '
# //       '###'
# //   steps(4)
# //       '#   '
# //       '##  '
# //       '### '
# //       '####'


def steps(num, count=1):
    if count == num:
        print('#' * count)
        return
    print(("#" * count) + " " * (num - count))
    steps(num, count + 1)


steps(2)
print("another one")
steps(3)
print("another one")
steps(5)

# Iterative solution
# def steps(num):
#     count = 1
#     for i in range(num):
#         for j in range(count):
#             print("#", end='')
#         space = " " * (num - count)
#         print(space, end='')
#         count += 1
#         print("")
