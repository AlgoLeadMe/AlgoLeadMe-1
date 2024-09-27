from collections import deque 
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, target, dist = map(int, input().split())
    graph[start].append((target, dist))

def dijkstra(root):
    queue = deque()
    distance = [INF] * (N + 1)

    distance[root] = 0
    queue.append((root, 0))
    while queue:
        now, dist = queue.popleft()
        
        for target, cost in graph[now]:
            target_cost = dist + cost

            if distance[target] > target_cost:
                distance[target] = target_cost
                queue.append((target, target_cost))
    return distance

result = []
for i in range(1, N+1):
    go = dijkstra(i)[X]
    back = dijkstra(X)[i]
    result.append(go+back)

print(max(result))