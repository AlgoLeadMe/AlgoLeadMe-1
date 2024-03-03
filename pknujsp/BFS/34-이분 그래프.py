from sys import *
from collections import *


def bfs(start):
    q = deque([start])
    groups[start] = 1

    while q:
        curr = q.popleft()
        visited[curr] = True

        for adj in graph[curr]:
            if visited[adj]:
                continue

            if not groups[adj]:
                groups[adj] = -groups[curr]
                q.append(adj)
            elif groups[adj] == groups[curr]:
                return False
    return True


for _ in range(int(stdin.readline())):
    V, E = map(int, stdin.readline().split())
    graph = [[] for i in range(V + 1)]

    for _ in range(E):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    groups = [0] * (V + 1)
    visited = [False] * (V + 1)
    result = None

    for i in range(1, V + 1):
        if groups[i] == 0 and not bfs(i):
            result = 'NO'
            break

    print('YES' if not result else result)
