# Simplest implementation
def quicksort(l):
    if len(l) <= 1:
        return l
    p = l[0]
    left = [e for e in l[1:] if e <= p]
    right = [e for e in l[1:] if e > p]
    return quicksort(left) + [p] + quicksort(right)


l = [1, 3, 12, 12, 3, 2, 5]
assert(quicksort(l) == sorted(l))
