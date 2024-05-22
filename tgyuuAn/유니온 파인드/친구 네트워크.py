import sys
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

def find_parent(element, graph):
    if graph[element] == element: return element
    
    parent = graph[element]
    graph[element] = find_parent(parent, graph)
    return graph[element]

def union(first, second, graph, count):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    if x == y: return

    x, y = min(x, y), max(x, y)
    graph[y] = x
    count[x] += count[y]
    count[y] = 0
    return

T = int(input())

for _ in range(T):
    F = int(input())
    index = 1
    parent = defaultdict(str)
    count = defaultdict(lambda : 1)
    
    for _ in range(F):
        first, second = input().split()
        if parent[first] == "": parent[first] = first
        if parent[second] == "": parent[second] = second
        if parent[first] != parent[second]: union(first, second, parent, count)
        
        print(count[find_parent(first, parent)])
        