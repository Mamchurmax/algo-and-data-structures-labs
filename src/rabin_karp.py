def to_hash(pattern):
    value = 0
    pos = 0
    for i in pattern:
        value += ord(i) * 2 ** (len(pattern) - pos - 1)
        pos += 1
    return value


def rabin_karp(haystack, needle):
    len_of_needle = len(needle)
    len_of_haystack = len(haystack)
    needle_hash = to_hash(needle)
    haystack_hash = to_hash(haystack[:len_of_needle])
    indexes = []

    if not needle:
        return indexes

    for i in range(len_of_haystack - len_of_needle + 1):
        if haystack_hash == needle_hash:
            if haystack[i:i + len_of_needle] == needle:
                indexes.append(i)

        if i + len_of_needle <= len_of_haystack:
            haystack_hash = to_hash(haystack[i + 1:i + 1 + len_of_needle])

    return indexes
