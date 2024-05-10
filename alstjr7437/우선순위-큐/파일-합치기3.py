from heapq import *

t = int(input())

for _ in range(t):
    n = int(input()) 
    answer = 0
    heap = []

    for i in map(int, input().split()):
        heappush(heap, i)
    
    while len(heap) > 1 :
        temp = heappop(heap) + heappop(heap)
        heappush(heap, temp)
        answer += temp
    print(answer)