from heapq import *
from collections import defaultdict

total_node_count, total_edge_count = map(int,input().split(" "))

visited = [False for _ in range(total_node_count+1)]
distance_table = [int(1e9) for _ in range(total_node_count+1)]
link_table = defaultdict(lambda: defaultdict(lambda : int(1e9)))
    
for _ in range(total_edge_count):
    node1, node2, weight = map(int, input().split(" "))
    link_table[node1][node2] = weight
    link_table[node2][node1] = weight

specific_node1, specific_node2 = map(int, input().split(" "))
distance_table[1] = 0
heap = [[0,1]]

while heap:

    now_distance, now_node = heappop(heap)
    visited[now_node] = True

    for link_node in link_table[now_node]:

        if visited[link_node] == True:
            continue

        if distance_table[link_node] > now_distance + link_table[now_node][link_node]:

            distance_table[link_node] = now_distance + link_table[now_node][link_node]
            heappush(heap,[distance_table[link_node],link_node])

specific_node1_distance_table = [int(1e9) for _ in range(total_node_count+1)]
specific_node1_distance_table[specific_node1] = 0
visited = [False for _ in range(total_node_count+1)]
heap = [[0,specific_node1]]
while heap:

    now_distance, now_node = heappop(heap)
    visited[now_node] = True

    for link_node in link_table[now_node]:

        if visited[link_node] == True:
            continue

        if specific_node1_distance_table[link_node] > now_distance + link_table[now_node][link_node]:

            specific_node1_distance_table[link_node] = now_distance + link_table[now_node][link_node]
            heappush(heap,[specific_node1_distance_table[link_node],link_node])

specific_node2_distance_table = [int(1e9) for _ in range(total_node_count+1)]
specific_node2_distance_table[specific_node2] = 0
visited = [False for _ in range(total_node_count+1)]
heap = [[0,specific_node2]]
while heap:

    now_distance, now_node = heappop(heap)
    visited[now_node] = True

    for link_node in link_table[now_node]:

        if visited[link_node] == True:
            continue

        if specific_node2_distance_table[link_node] > now_distance + link_table[now_node][link_node]:

            specific_node2_distance_table[link_node] = now_distance + link_table[now_node][link_node]
            heappush(heap,[specific_node2_distance_table[link_node],link_node])

first_route = distance_table[specific_node1] + specific_node1_distance_table[specific_node2] + specific_node2_distance_table[total_node_count]
second_route = distance_table[specific_node2] + specific_node2_distance_table[specific_node1] + specific_node1_distance_table[total_node_count]

if first_route >= int(1e9) and second_route >= int(1e9):
    print(-1)

elif first_route < second_route:
    print(first_route)

else:
    print(second_route)