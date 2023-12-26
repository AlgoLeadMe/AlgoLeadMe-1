import heapq

def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1]) 
    while heap:
        cost, node = heapq.heappop(heap)
        for next_cost, next_node in adj[node]:
            if cost + next_cost < dist[next_node]:
                dist[next_node] = cost + next_cost
                heapq.heappush(heap, [cost + next_cost, next_node])

def solution(N, road, K):
    dist = [float('inf')] * (N + 1)  
    dist[1] = 0  
    adj = [[] for _ in range(N + 1)]

    for r in road:
        adj[r[0]].append([r[2], r[1]]) 
        adj[r[1]].append([r[2], r[0]])

    dijkstra(dist, adj)

    answer = len([i for i in dist if i <= K])
    return answer