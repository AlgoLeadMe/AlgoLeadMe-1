from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()

N, M, T = map(int, input().split())
board = []

for _ in range(N):
    board.append(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
heap = [(0, 0, 0)]
answer = int(1e9)
visited = {(0,0),}
while heap:
    now_time, now_row, now_col = heappop(heap)
    
    if now_row == N-1 and now_col == M-1:
        answer = min(answer, now_time)
        break
    
    if now_time >= T: continue

    for dir in range(4):
        new_row = now_row + dy[dir]
        new_col = now_col + dx[dir]
        
        if new_row < 0 or new_row >= N: continue
        if new_col < 0 or new_col >= M: continue
        if (new_row, new_col) in visited: continue
    
        if board[new_row][new_col] == "2":
            heappush(heap, (now_time+1, new_row, new_col))
            answer = min(answer, (now_time+1+(N-1-new_row)+(M-1-new_col)))
            
        elif board[new_row][new_col] == "0":
            heappush(heap, (now_time+1, new_row, new_col))
            
        visited.add((new_row, new_col))

print(answer) if answer <= T else print("Fail")