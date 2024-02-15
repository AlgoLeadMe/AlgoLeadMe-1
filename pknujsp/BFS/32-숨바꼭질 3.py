from sys import *
from collections import *

n, k = map(int, stdin.readline().strip().split())

max_idx = 100001

q = deque([(n, 0)])
visited = [False] * max_idx
visited[n] = True

while q:
    x, cost = q.popleft()
    if x == k:
        print(cost)
        break

    nx = x + x
    if nx < max_idx and not visited[nx]:
        visited[nx] = True
        q.appendleft((nx, cost))

    nx = x - 1
    if 0 <= nx and not visited[nx]:
        visited[nx] = True
        q.append((nx, cost + 1))

    nx = x + 1
    if nx < max_idx and not visited[nx]:
        visited[nx] = True
        q.append((nx, cost + 1))
