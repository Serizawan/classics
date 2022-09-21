def merge_sort(l):
    if len(l) == 1:
        return l
    l1, l2 = l[:len(l) // 2], l[len(l) // 2:]
    l1_sorted = merge_sort(l1)
    l2_sorted = merge_sort(l2)
    l_sorted = []
    while l1_sorted and l2_sorted:
        if l1_sorted[0] <= l2_sorted[0]:
            l_sorted.append(l1_sorted.pop(0))
        else:
            l_sorted.append(l2_sorted.pop(0))
    return l_sorted + l1_sorted + l2_sorted


if __name__ == "__main__":
    l = [1, 3, 12, 12, 3, 2, 5]
    assert(merge_sort(l) == sorted(l) == [1, 2, 3, 3, 5, 12, 12])