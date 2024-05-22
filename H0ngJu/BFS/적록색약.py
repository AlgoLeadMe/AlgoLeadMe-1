import sys
sys.setrecursionlimit(10**6)
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())
arr = [[i for i in input()]for _ in range(N)]
visited = [[0] * N for _ in range(N)]
direc = [(1,0), (-1,0), (0,1), (0,-1)]
result = [0, 0]

def bfs(x, y, color):
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in direc:
            nx = dx + cx
            ny = dy + cy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = 1


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,arr[i][j])
            result[0] += 1

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == "R":
            arr[i][j] = "G"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,arr[i][j])
            result[1] += 1


print(result[0], result[1], end=" ")