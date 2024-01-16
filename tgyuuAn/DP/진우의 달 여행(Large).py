N, M = map(int,input().split())

dp_table = [[[int(1e9),int(1e9),int(1e9)] for _ in range(M)] for _ in range(N)]

board = []
for idx in range(N):
    board.append(list(map(int,input().split())))

for idx, element in enumerate(board[0]):
    dp_table[0][idx] = [element for _ in range(3)]

# print(dp_table)
# print(board)

dx = [-1,0,1]
dy = [1,1,1]

for y in range(N-1):
    for x in range(M):
        for check in range(3):
            for direction in range(3):
                # 이전에 진행했던 방향이면 continue
                if check == direction:
                    continue

                new_y, new_x = y+1, x + dx[direction]

                if new_x < 0 or new_x >= M:
                    continue

                if dp_table[new_y][new_x][direction] > dp_table[y][x][check] + board[new_y][new_x]:
                    dp_table[new_y][new_x][direction] = (dp_table[y][x][check]+board[new_y][new_x])

            # for dp in dp_table:
            #     print(dp)
            # print()

answer = int(1e9)
for last_x in dp_table[-1]:
    for last_element in last_x:
        answer = min(answer , last_element)

print(answer)