import heapq
from collections import defaultdict

def solution(n, edge):
    heap = [[0,1]]
    distance = [int(1e9) for _ in range(n+1)]
    flag = [False for _ in range(n+1)]
    graph = defaultdict(set)
    
    flag[1] = True
    distance[1] = 0

    for start, destination in edge:
        graph[start].add(destination)
        graph[destination].add(start)
            
    while heap:
        cost,now = heapq.heappop(heap)
        
        for node in graph[now]:
            if not flag[node]:
                distance[node] = min(distance[node], cost+1)
                heapq.heappush(heap,[distance[node],node])
                flag[node] = True
            
    _max = max(distance[1:])
    count = 0
    for x in distance[1:]:
        if x == _max:
            count += 1

    return count