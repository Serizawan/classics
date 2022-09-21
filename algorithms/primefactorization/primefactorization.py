from functools import reduce
from operator import mul


def prime_factorize(n):
    d = 2
    res = []
    while d * d <= n:
        if n % d == 0:
            n //= d
            res.append(d)
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res


if __name__ == "__main__":
    result = [2, 3, 5, 5, 7, 11]
    n = reduce(mul, result)
    assert(prime_factorize(n) == result)
