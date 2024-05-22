from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int, input().split())
tomato = []
visited = [[0] * n for _ in range(m)]

for _ in range(m):
    tomato.append(list(map(int, input().split())))

queue = deque()

for y in range(m):
    for x in range(n):
        if tomato[y][x] == 1:
            queue.append((y,x))
            visited[y][x] = 1

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if tomato[ny][nx] != -1 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            tomato[ny][nx] = tomato[y][x] + 1
            queue.append((ny, nx))

if any(0 in l for l in tomato):
    print(-1)
else : 
    test = max(map(max, tomato))
    print(test - 1) 
