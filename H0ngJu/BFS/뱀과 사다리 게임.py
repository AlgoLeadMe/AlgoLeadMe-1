import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]
game = [i for i in range(1,101)]
visited = [0 for _ in range(100)]
q = deque()

q.append((1,0))
visited[0] = 1

while q:
    cur, dice = q.popleft()
    if cur == 100:
        print(dice)
        break
    for i in range(1, 7):
        check = 0
        
        if cur + i > 100: continue

        # 사다리 갈 수 있는지 검사
        for l, n in ladder:
            if cur + i == l:
                if visited[n-1] == 0:
                    q.append((n, dice+1))
                    visited[n-1] = 1
                check = 1
                break

        if check: continue
        # 뱀 있는지 검사
        for s, n in snake:
            if cur + i == s:
                if visited[n-1] == 0:
                    q.append((n, dice+1))
                    visited[n-1] = 1
                check = 1
                break

        if check: continue 
        # 그 외 
        if visited[cur + i-1] == 0:
            q.append((cur + i, dice + 1))
            visited[cur + i-1] = 1