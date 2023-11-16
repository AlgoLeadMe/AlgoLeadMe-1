INT_MAX = 1_000_000


def solution(x, y, n):
    return min_count(x, y, n)


def min_count(x, y, n):
    vals = [INT_MAX for _ in range(y + 1)]
    vals[x] = 0

    for i in range(x, y + 1):
        if vals[i] != INT_MAX:
            val = vals[i] + 1
            idx = i + n

            if idx <= y:
                vals[idx] = min(val, vals[idx])

            idx = i * 2
            if idx <= y:
                vals[idx] = min(val, vals[idx])

            idx = i * 3
            if idx <= y:
                vals[idx] = min(val, vals[idx])

    return vals[y] if vals[y] != INT_MAX else -1
