from collections import defaultdict, deque
from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
ant = [int(input()) for _ in range(N)]
graph_info = defaultdict(lambda : defaultdict(int))
neighbor_count = [0 for _ in range(N+1)]

for _ in range(N-1):
    start, destination, cost = map(int, input().split())
    graph_info[start][destination] = cost
    graph_info[destination][start] = cost

    neighbor_count[start] += 1
    neighbor_count[destination] += 1

cost = [int(1e9) for _ in range(N+1)]
heap = [(0,1)]
parent = [0 for idx in range(N+1)]

while heap:
    now_cost, now_node = heappop(heap)

    if now_cost >= cost[now_node] and now_node != 1: continue
    cost[now_node] = now_cost
            
    for next_node, next_cost in graph_info[now_node].items():
        if now_cost + next_cost < cost[next_node]:
            heappush(heap, (now_cost + next_cost, next_node))
            parent[next_node] = now_node

leaf_node = deque()
for node, value in enumerate(neighbor_count):
    if node in (0, 1): continue
    if value == 1: leaf_node.append(node)

#print(leaf_node)

def check(mid, now_road, energy):
    if now_road[0][1] - now_road[mid][1] <= energy: return True
    return False

answer = [0 for _ in range(N+1)]

#print()
#print(ant)
for leaf in leaf_node:
    now_node = leaf
    now_road = deque()
    while now_node != 0:
        now_road.append((now_node, cost[now_node]))
        now_node = parent[now_node]
    
    while now_road:
        now_idx, now_distance = now_road[0]
        now_energy = ant[now_idx-1]

        if answer[now_idx] != 0:
            now_road.popleft()
            continue
        
       # print(now_road)
        
        left = -1
        right = len(now_road)
        temp = 0
        while left+1<right:
            mid = (left+right)//2
            #print(left, mid, right)

            if check(mid, now_road, now_energy):
                temp = mid
                left = mid

            else: right = mid

        answer[now_idx] = now_road[temp][0]
        #print(answer[1:])
        #print()
        now_road.popleft()

for ans in answer[1:]: print(ans)