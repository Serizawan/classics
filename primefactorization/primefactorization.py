def primefactorization(n):
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
