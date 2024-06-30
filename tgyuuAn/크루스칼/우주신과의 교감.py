from itertools import combinations
from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()

def find_parent(graph, element):
    if graph[element] == element: return element
    parent = graph[element]
    graph[element] = find_parent(graph, parent)
    
    return graph[element]

def union(graph, first, second):
    x = find_parent(graph, first)
    y = find_parent(graph, second)

    x, y = min(x, y), max(x, y)
    graph[y] = x
    return

def calculate_distance(first, second):
    return (abs(first[0] - second[0])**2 + abs(first[1] - second[1])**2)**0.5

N, M = map(int,input().split())

parent_graph = [x for x in range(N+1)]

space_gods = [0]
for _ in range(N):
    x, y = map(int, input().split())
    space_gods.append((x, y))

answer = 0
for _ in range(M):
    first, second = map(int, input().split())
    union(parent_graph, first, second)

heap = []
for elements in combinations(range(1,N+1),2):
    distance_gap = calculate_distance(space_gods[elements[0]],space_gods[elements[1]])
    heappush(heap, (distance_gap, elements[0], elements[1]))

while heap:
    now_distance, first, second = heappop(heap)
    
    if find_parent(parent_graph, first) == find_parent(parent_graph, second): continue
    union(parent_graph, first, second)
    answer += now_distance

print(f"{round(answer,2):.2f}")