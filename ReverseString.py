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
