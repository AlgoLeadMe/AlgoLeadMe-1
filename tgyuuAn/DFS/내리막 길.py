import sys
sys.setrecursionlimit(10**6)

def input(): return sys.stdin.readline().rstrip()

M, N = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(M) ]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dp = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(now):
    if now == (N-1, M-1):
        return 1

    col, row = now
    now_value = board[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]

    temp = 0    
    for dir in range(4):
        new_col = col + dx[dir]
        new_row = row + dy[dir]
        
        if new_col < 0 or new_col > N-1: continue
        if new_row < 0 or new_row > M-1: continue
        if board[new_row][new_col] >= now_value: continue
    
        temp += dfs((new_col,new_row))
    
    dp[row][col] = temp
    return dp[row][col]
    
print(dfs((0,0)))