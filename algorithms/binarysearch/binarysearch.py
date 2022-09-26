def binary_search(l, x, idx):
    if len(l) == 0:
        return None

    mid_idx = len(l) // 2
    if x == l[mid_idx]:
        return idx + mid_idx

    if x < l[mid_idx]:
        return binary_search(l[:mid_idx], x, idx)

    if x > l[mid_idx]:
        return binary_search(l[mid_idx + 1:], x, idx + mid_idx)


if __name__ == "__main__":
    l = [1, 2, 3, 5, 9, 21]
    assert(binary_search(l, 5, 0) == l.index(5) == 3)
    assert(not binary_search(l, 6, 0))
