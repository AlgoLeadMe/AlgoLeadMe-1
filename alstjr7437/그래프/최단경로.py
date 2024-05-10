from heapq import *
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

# 그래프 만들기
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  

# 결과 저장할 변수 만들기
heap = []
result = [int(1e9)] * (v + 1)

# k 넣기
result[k] = 0
heappush(heap, (0, k))  

# 다익스트라 돌리기
while heap:
    weight, now = heappop(heap)  
    # print(weight,now, heap, result)
    if result[now] < weight:
        continue
    for next_weight, next_node in graph[now]:
        total_weight = weight + next_weight
        if total_weight < result[next_node]:
            result[next_node] = total_weight
            heappush(heap, (total_weight, next_node))

# 결과 출력하기
for i in range(1, v + 1):
    if result[i] == int(1e9):
        print("INF")
    else:
        print(result[i])
