from collections import deque, defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [[False for _ in range(N+1)] for _ in range(N+1)]
board[1][1] = True

switch = defaultdict(list)

for _ in range(M):
    x, y, a, b = map(int, input().split())
    switch[(x, y)].append((a,b))
    
deq = deque()
deq.append((1,1))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = {(1, 1),}
dedicates = {(1, 1),}

while deq:
    now_x, now_y = deq.popleft()
    
    for turn_on in switch[(now_x, now_y)]:
        if turn_on not in dedicates:    # <<<------- 이 코드 한줄에 3시간 날림
            dedicates.add(turn_on)
        
            if turn_on in visited: 
                deq.append(turn_on)
        
    for dir in range(4):
        new_x = now_x + dx[dir]
        new_y = now_y + dy[dir]

        if new_x <= 0 or new_x >= N+1: continue
        if new_y <= 0 or new_y >= N+1: continue
        if (new_x, new_y) in visited: continue
        
        visited.add((new_x, new_y))
        
        if (new_x, new_y) in dedicates:
            deq.append((new_x, new_y))
            
print(len(dedicates))