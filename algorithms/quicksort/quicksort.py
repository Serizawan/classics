def quick_sort(l):
    if len(l) <= 1:
        return l
    p = l[0]
    left = [e for e in l[1:] if e <= p]
    right = [e for e in l[1:] if e > p]
    return quick_sort(left) + [p] + quick_sort(right)


if __name__ == "__main__":
    l = [1, 3, 12, 12, 3, 2, 5]
    assert(quick_sort(l) == sorted(l))
