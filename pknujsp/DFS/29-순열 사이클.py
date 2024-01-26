"""
DFS
"""

from sys import *


def find_cycles(graph):
    visited = [False] * (len(graph))
    cycles = 0

    for start in graph[1:]:
        if visited[start]:
            continue

        stack = [start]
        while stack:
            node = stack.pop()

            if visited[node]:
                cycles += 1
                break

            visited[node] = True
            stack.append(graph[node])

    return cycles


if __name__ == "__main__":
    T = int(stdin.readline())

    for _ in range(T):
        N = int(stdin.readline())
        graph = [0] * (N + 1)

        for a, b in zip(range(1, N + 1), stdin.readline().split()):
            graph[a] = int(b)

        cycles = find_cycles(graph)
        print(cycles)

"""
union-find
"""

from sys import *

setrecursionlimit(2000)


def find_parent(table, start, x):
    if table[x] == start:
        return start

    if table[x] != x:
        table[x] = find_parent(table, start, table[x])
    return table[x]


def is_on_cycle(graph, a, b):
    a = find_parent(graph, a, a)
    b = find_parent(graph, b, b)
    if a > b:
        graph[b] = a
    else:
        graph[a] = b

    return a == b


def find_cycles(graph):
    root_nodes = set()

    for a in range(1, len(graph)):
        parent = graph[a]
        if is_on_cycle(graph, a, parent):
            root_nodes.add(graph[a])

    return len(root_nodes)


if __name__ == "__main__":
    stdin = open("10451.txt")
    T = int(stdin.readline())

    for _ in range(T):
        N = int(stdin.readline())
        graph = [0] * (N + 1)

        for a, b in zip(range(1, N + 1), stdin.readline().split()):
            graph[a] = int(b)

        cycles = find_cycles(graph)
        print(cycles)
