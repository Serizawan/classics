def compute_partial_match_table(pattern):
    partial_match_table = [0]
    for i in range(1, len(pattern)):
        j = partial_match_table[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = partial_match_table[j - 1]
        partial_match_table.append(j + 1 if pattern[j] == pattern[i] else j)
    return partial_match_table


def kmp_search(pattern, text):
    partial_match_table = compute_partial_match_table(pattern)
    matching_indexes = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = partial_match_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matching_indexes.append(i - (j - 1))
            j = partial_match_table[j - 1]

    return matching_indexes


if __name__ == "__main__":
    assert(kmp_search("aab", "aaabaacbaab") == [1, 8])
