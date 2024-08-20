import sys
from collections import deque

def input() : return sys.stdin.readline().rstrip()

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dir = [(0,1), (0,-1), (1,0), (-1,0)]
x = 0
y = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[x][y] = 0

def check(a, b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

baby = 2

time = 0
fish = 0

while True:
    q = deque([(x, y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    min_dis = float('inf')
    tmp = []

    while q:
        cx, cy, dis = q.popleft()

        if 0 < space[cx][cy] < baby:
            if dis < min_dis:
                min_dis = dis
                tmp = [(cx, cy)]
            elif dis == min_dis:
                tmp.append((cx, cy))
        
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if check(nx, ny) and not visited[nx][ny] and space[nx][ny] <= baby:
                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))
        
    if not tmp:
        break

    tx, ty = min(tmp)
    space[tx][ty] = 0
    time += min_dis
    fish += 1
    if fish == baby:
        baby += 1
        fish = 0
    x, y = tx, ty

print(time)