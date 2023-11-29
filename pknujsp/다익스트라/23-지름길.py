from sys import *
from collections import *

stdin = open("1446.txt")

SHORTCUTS, HIGHWAY_LENGTH = map(int, stdin.readline().split())
START, TARGET = 0, HIGHWAY_LENGTH

graph = {START: {(TARGET, HIGHWAY_LENGTH)}, TARGET: set()}

for _ in range(SHORTCUTS):
    entrances, exits, length = map(int, stdin.readline().split())

    if exits <= TARGET:
        graph.setdefault(entrances, set()).add((exits, length))
        graph.setdefault(exits, set())

if len(graph) > 2:
    # 지름길이 있는 경우, 고속도로만 주행할 때 지나치는 각 노드 사이의 거리를 계산
    nodes = sorted(graph.keys())
    for i in range(1, len(nodes)):
        graph[nodes[i - 1]].add((nodes[i], nodes[i] - nodes[i - 1]))

MAX_INT = 100000
distances = {node: MAX_INT for node in graph}
distances[START] = 0
q = deque([START])

while q:
    node = q.popleft()
    driven_distance = distances[node]
    min_distance = MAX_INT

    for next_node, length in graph[node]:
        distances[next_node] = min(driven_distance + length, distances[next_node])
        min_distance = min(distances[next_node], min_distance)

    for next_node, _ in graph[node]:
        if distances[next_node] == min_distance:
            q.append(next_node)

print(distances[TARGET])
