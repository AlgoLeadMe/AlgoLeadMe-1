from collections import defaultdict
from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()
MAX = 100_000 * 700_000 + 1
N, M = map(int, input().split())

graph = defaultdict(lambda : defaultdict(list))

for idx in range(1,M+1):
    start, destination = map(int, input().split())
    graph[start][destination].append(idx)
    graph[destination][start].append(idx)
    
costs = [MAX for _ in range(N+1)]
visited = set()
heap = [(0, 1)]
while heap:
    now_cost, now_idx = heappop(heap)
    
    if now_idx in visited: continue
    visited.add(now_idx)
    
    if costs[now_idx] <= now_cost: continue
    costs[now_idx] = now_cost
    
    if now_idx == N: break

    for neighbor in graph[now_idx]:
        if neighbor in visited: continue
        
        for neighbor_idx in graph[now_idx][neighbor]:
    
            real_idx = now_cost % M
            if real_idx < neighbor_idx:
                heappush(heap, (neighbor_idx - real_idx + now_cost, neighbor))
            else:
                heappush(heap, (now_cost + M - real_idx + neighbor_idx, neighbor))
print(costs[-1])