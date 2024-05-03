from collections import defaultdict, deque
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())

    costs = [[int(1e9) for _ in range(M+1)] for _ in range(N+1)]
    costs[1][0] = 0

    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        start, destination, cost, duration = map(int,input().split())
        graph[start].append((destination, cost, duration))

    # print(edges)

    for cost in range(M+1):
        for city in range(1, N):
            if costs[city][cost] == int(1e9): continue

            for now_destination, now_cost, now_duration in graph[city]:

                if now_cost + cost <= M and costs[now_destination][cost + now_cost] > costs[city][cost] + now_duration: 
                    costs[now_destination][cost + now_cost] = costs[city][cost] + now_duration

    result = min(costs[N])
    print(result) if result != int(1e9) else print("Poor KCM")