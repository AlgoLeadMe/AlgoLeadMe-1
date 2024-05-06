import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())

board = []
idx = 1
for row in range(N):
    row_tiles = []
    # 홀수 줄 일 경우 N개가 그대로 들어옴
    if row%2==0:
        for col in range(N):
            temp = list(input().split())
            temp.append(idx)
            tile = tuple(temp)
        
            row_tiles.append(tile)
            idx += 1

    # 짝수 줄 일 경우 N-1개가 들어옴
    else:
        for col in range(N-1):
            temp = list(input().split())
            temp.append(idx)
            tile = tuple(temp)
            
            row_tiles.append(tile)
            idx += 1

    board.append(row_tiles)
    
parent_tile = [-1 for _ in range(idx)]

odd_dx = [-1, -1, 0, 0, 1, -1]
odd_dy = [0, 1, -1, 1, 0, 1]

even_dx = [0, 1, -1, 1, 0, 1]
even_dy = [-1, -1, 0, 0, 1, 1]

now = (1, (0, 0), 1) # 타일 번호, 현재 타일 좌표, 현재 이동한 횟수
visited = set()
deq = deque([now])
biggest_number_tile = -1
biggest_number_count = int(1e9)
while deq:
    now_tile, tile_pos, now_count = deq.popleft()
    now_x = tile_pos[0]
    now_y = tile_pos[1]
    
    if now_tile > biggest_number_tile:
        biggest_number_tile = now_tile
        biggest_number_count = now_count
    
    if now_tile == idx-1:
        print(now_count)
        ans_que = deque([])
        now = now_tile
        while now != 1:
            ans_que.appendleft(now)
            now = parent_tile[now]
        ans_que.appendleft(1)
        print(*ans_que)
        break
    
    # 홀수번 째 줄 일 경우,
    if now_y%2 == 0:
        
        for dir in range(6):
            new_x = now_x + odd_dx[dir]
            new_y = now_y + odd_dy[dir]
            
            if new_x < 0 or new_x >= N: continue
            if new_y%2 == 1 and new_x >= N-1: continue
            if new_y < 0 or new_y >= N: continue
            
            new_tile = board[new_y][new_x]
            new_tile_idx = new_tile[-1]

            if new_tile_idx in visited: continue
            if dir in (0,1,5) and board[now_y][now_x][0] != board[new_y][new_x][1]: continue
            if dir in (2,3,4) and board[now_y][now_x][1] != board[new_y][new_x][0]: continue
        
            visited.add(new_tile_idx)
            parent_tile[new_tile_idx] = now_tile
            deq.append((new_tile_idx, (new_x, new_y), now_count+1))
    
    # 짝수번 째 줄 일 경우,
    else:
        for dir in range(6):
            new_x = now_x + even_dx[dir]
            new_y = now_y + even_dy[dir]
            
            if new_x < 0 or new_x >= N: continue
            if new_y%2 == 1 and new_x >= N-1: continue
            if new_y < 0 or new_y >= N: continue
            
            new_tile = board[new_y][new_x]
            new_tile_idx = new_tile[-1]

            if new_tile_idx in visited: continue
            if dir in (0,2,4) and board[now_y][now_x][0] != board[new_y][new_x][1]: continue
            if dir in (1,3,5) and board[now_y][now_x][1] != board[new_y][new_x][0]: continue
        
            visited.add(new_tile_idx)
            parent_tile[new_tile_idx] = now_tile
            deq.append((new_tile_idx, (new_x, new_y), now_count+1))
            
else:
    print(biggest_number_count)
    ans_que = deque([])
    now = biggest_number_tile
    while now != 1:
        ans_que.appendleft(now)
        now = parent_tile[now]
    ans_que.appendleft(1)
    print(*ans_que)
    
# 홀수번 째 줄에서 이동할 때,
# 짝수번 째 줄로 행 이동을 할 때에는 N번째 인덱스 뿐 아니라 N-1번째 인덱스로도 접근 가능.
# 당연하겠지만 열의 0번 인덱스에서는 0번으로만 이동할 수 있음.
# 마찬가지로 열의 마지막 인덱스에서는 N-1로만 이동할 수 있음.

# 짝수번 째 줄에서 홀수번 째 줄으로 행 이동할 때에는,
# N번째 줄 뿐아니라, N+1번째 줄로도 이동 가능.