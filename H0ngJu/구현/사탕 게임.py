import sys

def input(): return sys.stdin.readline().rstrip()

def eat(row, col):
    row_cnt = 0
    col_cnt = 0
    tmp_col = 1
    tmp_row = 1
    for idx in range(N-1):
        # 열에서 먹을 때
        if data[row][idx] == data[row][idx+1]:
            tmp_col += 1
            col_cnt = max(col_cnt, tmp_col)
        else:
            tmp_col = 1

        # 행에서 먹을 때
        if data[idx][col] == data[idx+1][col]:
            tmp_row += 1
            row_cnt = max(row_cnt, tmp_row)
        else:
            tmp_row = 1

    return max(row_cnt, col_cnt)
    

N = int(input())
data = [[x for x in input()] for _ in range(N)]
directions = [(0,-1), (0,1), (-1,0),(1,0)]
cnt = 0

for i in range(N):
    for k in range(N):
        for dir in directions:
            dx, dy = dir
            x = i+dx
            y = k+dy
            if 0<=x<N and 0<=y<N:
                data[i][k], data[x][y] = data[x][y], data[i][k]
                cnt = max(cnt, eat(x,y))
                data[i][k], data[x][y] = data[x][y], data[i][k] #다시 되돌리기

print(cnt)