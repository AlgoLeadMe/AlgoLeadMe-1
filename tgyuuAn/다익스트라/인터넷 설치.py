import sys
from heapq import *

def input(): return sys.stdin.readline().rstrip()

N, P, K = map(int, input().split())
graph = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]

for _ in range(P):
    start, destination, cost = map(int, input().split())
    graph[start][destination] = min(graph[start][destination], cost)
    graph[destination][start] = min(graph[destination][start], cost)

def check(mid):
    if dijkstra(mid): return True
    return False

def dijkstra(_max):
    visited = set()
    DP = [[int(1e9) for _ in range(K+1)] for _ in range(N+1)]
    DP[1][K] = 0
    
    # 간선 코스트, 남은 기회, 현재 노드
    heap = [(0, K, 1)]
    while heap:
        now_cost, now_remain, now_node = heappop(heap)
        
        if (now_node, now_remain) in visited: continue
        visited.add((now_node, now_remain))
        
        if DP[now_node][now_remain] < now_cost: continue
        DP[now_node][now_remain] = now_cost

        if now_node == N:
            return True
    
        for idx, cost in enumerate(graph[now_node]):
            if idx == 0: continue
            if cost == int(1e9): continue
            
            if cost <= _max:
                if (idx, now_remain) in visited: continue
                if DP[idx][now_remain] > cost: heappush(heap, (cost, now_remain, idx))
                
            elif cost > _max and now_remain >= 1: 
                if (idx, now_remain-1) in visited: continue
                if DP[idx][now_remain-1] > cost: heappush(heap, (cost, now_remain-1, idx))    
    
    for idx in range(1, K+1):
        if DP[N][idx] != int(1e9): return True
    
    return False
    
answer = int(1e9)
left = -1
right = 1_000_001 
while left+1<right:
    mid = (left + right) // 2
    
    if check(mid): 
        right = mid
        answer = mid
    else: left = mid

if answer != int(1e9): print(answer)
else: print(-1)