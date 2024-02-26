def pumpkin(m, n):
    result = []
    for i in range(m):
        if i % 2 == 0:
            result.extend(list(range(i * n + 1, (i + 1) * n + 1)))
        else:
            result.extend(list(range((i + 1) * n, i * n, -1)))
    return result


print(pumpkin(4, 4))
