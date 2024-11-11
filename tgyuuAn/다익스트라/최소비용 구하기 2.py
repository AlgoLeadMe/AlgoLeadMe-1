from heapq import *
from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
bus_info = defaultdict(lambda : defaultdict(lambda : int(1e9)))

for _ in range(M):
    n1, n2, cost = map(int,input().split())
    
    if bus_info[n1][n2] > cost: 
        bus_info[n1][n2] = cost

start, destination = map(int, input().split())
heap = []
heappush(heap, [0, 0, start])

previous = [1 for _ in range(N+1)]
cost = [int(1e9) for _ in range(N+1)]
while heap:
    now_cost, previous_node, now_node = heappop(heap)
    
    if cost[now_node] <= now_cost: continue
    previous[now_node] = previous_node
    cost[now_node] = now_cost

    for node in bus_info[now_node]:
        temp = now_cost + bus_info[now_node][node]
        if cost[node] > temp:
            heappush(heap, [temp, now_node, node])

print(cost[destination])

history = []
now_history = destination
while now_history != 0:
    history.append(now_history)
    now_history = previous[now_history]
    
print(len(history))
print(" ".join(map(str, history[-1::-1])))