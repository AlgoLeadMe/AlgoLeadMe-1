def swap(player):
    return player == 'O' and 'X' or 'O'

def end(board):
    for line in board:
        if line == 'OOO' or line == 'XXX': return True
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != '.': return True
        
    if board[0][0] == board[1][1] == board[2][2] != '.': return True

    if board[0][2] == board[1][1] == board[2][0] != '.': return True
    
    return False

def solution(board):
    def dfs(player, newBoard):
        if (board == newBoard): return True
        if (end(newBoard)): return False
        for i, line in enumerate(newBoard):
            for j, cell in enumerate(line):
                if cell != '.': continue
                temp = newBoard[i]
                newBoard[i] = newBoard[i][:j] + player + newBoard[i][j+1:]
                if dfs(swap(player), newBoard): return True
                newBoard[i] = temp
        return False
    emptyBoard = ['.' * 3 for _ in range(3)]
    return int(dfs('O', emptyBoard))