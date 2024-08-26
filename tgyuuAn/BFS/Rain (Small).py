from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for test_idx in range(T):
    row, col = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(row)]
    new_board = [[0 for _ in range(col)] for _ in range(row)]

    for height in range(1, 1001):
        for start_row in range(row):
            for start_col in range(col):
                if board[start_row][start_col] >= height: continue
                
                deq = deque()
                deq.append((start_row, start_col))
                history = {(start_row, start_col),}
                
                visited = set()
                visited.add((start_row, start_col))
                
                while deq:
                    now_row, now_col = deq.popleft()
                    
                    # 가장자리에 물이 흘렀다는 것이므로 break
                    if now_row in (0, row-1): break
                    if now_col in (0, col-1): break

                    for dir in range(4):
                        new_row = now_row + dy[dir]
                        new_col = now_col + dx[dir]

                        if new_row < 0 or new_row >= row: continue
                        if new_col < 0 or new_col >= col: continue
                        if (new_row, new_col) in visited: continue
                        if board[new_row][new_col] >= height: continue
                    
                        deq.append((new_row, new_col))
                        history.add((new_row, new_col))
                        visited.add((new_row, new_col))
                    
                    # 가장자리에 물이 흐르지 않아 break되지 않았으면,
                else:
                    for history_row, history_col in history:
                        new_board[history_row][history_col] = height - board[history_row][history_col]

    print(f"Case #{test_idx+1}: {sum([sum(row) for row in new_board])}")