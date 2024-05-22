from collections import defaultdict
from heapq import *
import sys

INF = 50_000_001

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    cnt_node, cnt_edge, cnt_dedication = map(int, input().split())
    start_node, g, h = map(int, input().split())
    
    graph = defaultdict(lambda : defaultdict(int))
    for _ in range(cnt_edge):
        start, destination, cost = map(int,input().split())
        graph[start][destination] = cost
        graph[destination][start] = cost

    node_dedications = set()
    for _ in range(cnt_dedication):
        node_dedications.add(int(input()))

    table = [INF for _ in range(cnt_node+1)]
    table[start_node] = 0
    
    visited = set()
    heap = []
    heappush(heap, [0, start_node, 1])
    flag = [1 for _ in range(cnt_node+1)]
    
    while heap:
        now_cost, now_node, now_flag = heappop(heap)

        if now_node in visited: continue
        visited.add(now_node)
        
        if flag[now_node] == 1 and now_flag == 0: flag[now_node] = 0

        for next_node in graph[now_node]:
            cost = graph[now_node][next_node]

            if (now_cost + cost) > table[next_node]: continue
            
            table[next_node] = now_cost + cost
            
            new_flag = now_flag
            # 만약, 지금 움직이려는 도로가 냄새가 나는 도로였을 경우 flag를 0로 바꿈
            if (now_node, next_node) in {(g, h), (h, g)}: new_flag = 0
    
            heappush(heap, [now_cost + cost, next_node, new_flag])

    answer = []
    for dedication in node_dedications:
        if flag[dedication] == 0: answer.append(dedication)
        
    print(*sorted(answer))