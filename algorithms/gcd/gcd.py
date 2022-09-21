import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a = 3 * 3 * 5 * 5 * 13
    b = 2 * 3 * 5 * 7 * 11
    assert(math.gcd(a, b) == gcd(a, b) == 3 * 5)
