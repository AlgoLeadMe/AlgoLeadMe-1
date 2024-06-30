from itertools import product
from copy import deepcopy
import sys

N = 10
INF = int(1e9)
board = [list(input()) for _ in range(N)]
answer = INF

def push(board, y, x):
    dx = [0, 0, 0, -1, 1]
    dy = [0, -1, 1, 0, 0]

    for dir in range(5):
        new_y = y + dy[dir]
        new_x = x + dx[dir]

        if new_y < 0 or new_y >= N: continue
        if new_x < 0 or new_x >= N: continue

        board[new_y][new_x] = "O" if board[new_y][new_x] == "#" else "#"

for first_row_pushed in product(range(2), repeat = N):
    new_board = deepcopy(board)
    count = 0

    for idx, pushed in enumerate(first_row_pushed):
        if pushed == True:
            count += 1
            push(new_board, 0, idx)

    for y in range(1, N):
        for x in range(N):
            if new_board[y-1][x] == "O":
                count += 1
                push(new_board, y, x)

    if all(element == "#" for element in new_board[-1]): answer = min(answer, count)

print(answer if answer != INF else -1)