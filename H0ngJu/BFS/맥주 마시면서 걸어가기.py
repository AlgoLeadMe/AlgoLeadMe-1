import sys
from collections import deque

def input() : return sys.stdin.readline().rstrip()

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())

    x, y = hx, hy
    result = "sad"

    q = deque([(x, y, 20)])
    visited = set([x, y])

    while q:
        x, y, beer = q.popleft()
       
        if abs(x-fx) + abs(y-fy) <= 50*beer: # 축제까지 갈 수 있는지
            result = "happy"
            break
        
        for sx, sy in store: # 편의점 들릴 수 있는지
            if abs(x-sx) + abs(y-sy) <= 50 * beer and (sx, sy) not in visited:
                visited.add((sx, sy))
                q.append((sx, sy, 20))
        
        if beer > 0: # beer 먹고 가기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, beer - 1))
    
    print(result)
    