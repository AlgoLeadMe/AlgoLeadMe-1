import sys

def input(): return sys.stdin.readline().rstrip()

board = []

for _ in range(9): board.append(list(input()))
                    
def dfs(board, now_row, now_col):
    
    # 이미 들어있는 칸일 경우
    if board[now_row][now_col] != "0":
        new_row = now_row
        new_col = now_col + 1

        if new_col >= 9:
            new_col = 0
            new_row += 1
        
        # 스도쿠 완성
        if new_row >= 9: return board
                    
        temp = dfs(board, new_row, new_col)

        if temp is not None: return temp
    
    # 비어있는 칸일 경우
    else:
        need_number = { str(x) for x in range(1,10) }
        
        # 가로 행 검사 
        for col in range(9):
            if board[now_row][col] != "0":
                need_number.discard(board[now_row][col])

        # 세로 행 검사
        for row in range(9):
            if board[row][now_col] != "0":
                need_number.discard(board[row][now_col])

        # 3X3 검사
        temp_row = (now_row//3)*3
        temp_col = (now_col//3)*3
        for inner_row in range(temp_row, temp_row+3):
            for inner_col in range(temp_col, temp_col+3):
                if board[inner_row][inner_col] != "0":
                    need_number.discard(board[inner_row][inner_col])
        
        # 만약 넣을 수 있는것이 없으면 None을 리턴   
        if len(need_number) == 0: return None
        
        need_number = sorted(list(map(int,need_number)))
        
        for dedicate_number in need_number:
            board[now_row][now_col] = str(dedicate_number)
            
            new_row = now_row
            new_col = now_col + 1
        
            if new_col >= 9:
                new_col = 0
                new_row += 1
            
            # 스도쿠 완성
            if new_row >= 9: return board     
        
            temp = dfs(board, new_row, new_col)

            if temp is not None: return temp
            
            board[now_row][now_col] = "0"
            
    return None
            
answer = dfs(board, 0, 0)

for row in answer:
    print("".join(row))