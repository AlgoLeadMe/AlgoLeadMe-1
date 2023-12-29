from collections import deque

def solution(board):
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    len_row = len(board)
    len_col = len(board[0])
        
    visited = [[True for _ in range(len_col)] for _ in range(len_row)]
    
    start_col, start_row = 0,0
    
    for idx_row in range(len_row):
        for idx_col in range(len_col):
            
            if board[idx_row][idx_col] == "D":
                visited[idx_row][idx_col] = False
            
            if board[idx_row][idx_col] == "R":
                visited[idx_row][idx_col] = False
                start_col = idx_col
                start_row = idx_row
    
    deq = deque([[start_row,start_col,0]])
    
    while deq:
        now = deq.popleft()
        now_row, now_col, now_count = now[0], now[1], now[2]
        
        if board[now_row][now_col] == "G":
            return now_count
        
        for idx in range(4):
    
            new_row, new_col = now_row, now_col    
            
            while True:
                new_row += dy[idx]
                new_col += dx[idx]
                
                if new_col == -1:
                    new_col = 0
                    break
                    
                elif new_col == len_col:
                    new_col = len_col-1
                    break
                    
                elif new_row == -1:
                    new_row = 0
                    break
                    
                elif new_row == len_row:
                    new_row = len_row-1
                    break
                    
                elif board[new_row][new_col] == "D":
                    new_col -= dx[idx]
                    new_row -= dy[idx]
                    break
        
            if visited[new_row][new_col] == True:
                deq.append([new_row,new_col,now_count+1])
                visited[new_row][new_col] = False
                
    return -1