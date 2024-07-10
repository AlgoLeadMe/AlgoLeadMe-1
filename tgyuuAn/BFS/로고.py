import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())

can_visit = set()
for _ in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    
    x1 *= 2
    y1 *= 2
    x2 *= 2
    y2 *= 2
    
    for draw_x in range(x1, x2+1):
        can_visit.add((draw_x, y1))
        can_visit.add((draw_x, y2))
        
    for draw_y in range(y1, y2+1):
        can_visit.add((x1, draw_y))
        can_visit.add((x2, draw_y))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
can_visit.add((0, 0))
draw_coordinate = deque(can_visit)
answer = 0
while draw_coordinate:
    deq = deque()

    if (0, 0) in can_visit: 
        deq.append((0, 0))
        can_visit.discard((0, 0))
        
    else:
        now_x, now_y = draw_coordinate.popleft()
        if (now_x, now_y) not in can_visit: continue
        
        deq.append((now_x, now_y))
        can_visit.discard((now_x, now_y))

    while deq:
        now_x, now_y = deq.popleft()

        for dir in range(4):
            new_x = now_x + dx[dir]
            new_y = now_y + dy[dir]

            if (new_x, new_y) not in can_visit: continue

            can_visit.discard((new_x, new_y))
            deq.append((new_x, new_y))

    answer += 1

print(answer-1)