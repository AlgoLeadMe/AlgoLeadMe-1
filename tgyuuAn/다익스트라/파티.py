from heapq import *
from collections import defaultdict

total_node_count, total_edge_count, target_node = map(int,input().split(" "))

visited = [False for _ in range(total_node_count+1)]
go_distance_table = [int(1e9) for _ in range(total_node_count+1)]
link_table = defaultdict(lambda: defaultdict(lambda : int(1e9)))


for _ in range(total_edge_count):
    node1, node2, weight = map(int, input().split(" "))
    link_table[node1][node2] = weight

#집에서 X로 가는 길
for idx in range(1,total_node_count+1):
    if idx == target_node:
        go_distance_table[target_node] = 0
        continue

    heap = [[0,idx]]
    temp_visited = [False for _ in range(total_node_count+1)]
    temp_distance_table = [int(1e9) for _ in range(total_node_count+1)]
    temp_distance_table[idx] = 0
    
    while heap:
        now_distance, now_node = heappop(heap)
        temp_visited[now_node] = True

        for link_node in link_table[now_node]:
            if temp_visited[link_node] == True:
                continue

            if temp_distance_table[link_node] > now_distance + link_table[now_node][link_node] :
                temp_distance_table[link_node] = now_distance + link_table[now_node][link_node]

                heappush(heap,[temp_distance_table[link_node],link_node])
    
    go_distance_table[idx] = temp_distance_table[target_node]

#X에서 집으로 돌아가는 길
come_distance_table = [int(1e9) for _ in range(total_node_count+1)]
heap = [[0,target_node]]

while heap:
    now_distance, now_node = heappop(heap)
    visited[now_node] = True

    for link_node in link_table[now_node]:
        if visited[link_node] == True:
            continue

        if come_distance_table[link_node] > now_distance + link_table[now_node][link_node] :
            come_distance_table[link_node] = now_distance +link_table[now_node][link_node]

            heappush(heap,[come_distance_table[link_node],link_node])

go_distance_table[target_node] = -1
come_distance_table[target_node] = -1
print(max([x+y for x,y in zip(go_distance_table[1:], come_distance_table[1:])]))