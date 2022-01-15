# // --- Directions
# // Given a string, return a new string with the reversed
# // order of characters
# // --- Examples
# //   reverse('apple') === 'leppa'
# //   reverse('hello') === 'olleh'
# //   reverse('Greetings!') === '!sgniteerG'

def reverse(str):
    reversed = ""
    for i in range(len(str)):
        reversed = str[i] + reversed
    return reversed


def test1():
    assert "dcba" == reverse("abcd")


def test2():
    assert "dcba  " == reverse("  abcd")


if __name__ == '__main__':
    test1()
    test2()
