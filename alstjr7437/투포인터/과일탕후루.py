N = int(input())
tanghuru = list(map(int, input().split()))
fruit = [0] * 10
kind = 0
start, end = 0, 0

while True:
    if end == N:
        print(end - start)
        break
    if fruit[tanghuru[end]] == 0:
        kind += 1
    fruit[tanghuru[end]] += 1
    end += 1

    if kind > 2:
        fruit[tanghuru[start]] -= 1
        if fruit[tanghuru[start]] == 0:
            kind -= 1
        start += 1


