from heapq import *
from sys import *

C, R = map(int, stdin.readline().split())
arr = [list(map(int, list(stdin.readline().strip()))) for _ in range(R)]

drc = ((1,0),(-1,0),(0,1),(0,-1))
visited = [[False] * C for _ in range(R)]
heap = [(0, 0, 0)]
target_r = R - 1
target_c = C - 1

while heap:
    cost, r, c = heappop(heap)

    if r == target_r and c == target_c:
        print(cost)
        break
    if visited[r][c]:
        continue      
        
    visited[r][c] = True
    
    for dr, dc in drc:
        nr = r + dr
        nc = c + dc

        if not 0 <= nr < R or not 0 <= nc < C:
            continue
        if visited[nr][nc]:
            continue
            
        heappush(heap, (cost + arr[nr][nc], nr, nc))
