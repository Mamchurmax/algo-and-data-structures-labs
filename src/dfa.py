def find_next_idx(pattern, idx, letter):
    if idx < len(pattern) and pattern[idx] == letter:
        return idx + 1
    else:
        current_idx = pattern[:idx] + letter
        for compare_len in range(idx, 0, -1):
            prefix = current_idx[:compare_len]
            suffix = current_idx[-compare_len:]
            if prefix == suffix:
                return compare_len
    return 0


def build_dfa(pattern):
    chars = list(set(pattern))
    finite_automata = [[0 for _ in range(len(chars))] for _ in range(len(pattern) + 1)]

    for idx in range(len(pattern) + 1):
        for i in range(len(chars)):
            finite_automata[idx][i] = find_next_idx(pattern, idx, chars[i])

    return finite_automata


def search_dfa(haystack, needle):
    dfa = build_dfa(needle)
    state = 0
    chars = list(set(needle))
    list_of_idx = []
    for i in range(len(haystack)):
        if haystack[i] in chars:
            state = dfa[state][chars.index(haystack[i])]
            if state == len(needle):
                list_of_idx.append(i - len(needle) + 1)
    return list_of_idx
