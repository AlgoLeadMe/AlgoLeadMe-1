from collections import deque
from copy import deepcopy

total_test_case = int(input())

for _ in range(total_test_case):
    height, width = map(int,input().split())

    _map = []
    start_point = []

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    #감옥 밖을 자유롭게 돌아다닐 수 있도록, 감옥 주변을 `.`` 으로 감싼다.
    _map.append(["." for _ in range(width+2)])

    for h in range(height):
        width_input = list("."+input()+".")
        _map.append(width_input)

        for w,w_input in enumerate(width_input):
            if w_input == "$":
                _map[h+1][w] = "."
                start_point.append((h+1,w))

    _map.append(["." for _ in range(width+2)])

    # 중간 체크
    # for h in range(height+2):
    #    print(_map[h])

    
    def bfs(start_h, start_w):
        deq = deque([(start_h, start_w)])
        open_door_table = [[-1 for _ in range(width+2)] for _ in range(height+2)]
        open_door_table[start_h][start_w] = 0

        while deq:
            now_h, now_w = deq.popleft()
            # print(now_h,now_w)

            for dir in range(4):
                new_h, new_w = now_h + dy[dir], now_w + dx[dir]

                if new_h < 0 or new_h > height +1:
                    continue

                if new_w < 0 or new_w > width +1:
                    continue

                if _map[new_h][new_w] == "*":
                    continue

                if open_door_table[new_h][new_w] != -1:
                    continue

                if _map[new_h][new_w] == ".":
                   deq.appendleft([new_h,new_w])
                   open_door_table[new_h][new_w] = open_door_table[now_h][now_w]

                elif _map[new_h][new_w] == "#":
                   deq.append([new_h,new_w])
                   open_door_table[new_h][new_w] = open_door_table[now_h][now_w] + 1

        return open_door_table

    open_door_table1 = bfs(start_point[0][0],start_point[0][1])
    open_door_table2 = bfs(start_point[1][0],start_point[1][1])
    open_door_table3 = bfs(0,0)

    # for h in range(height+2):
    #     print(open_door_table1[h])
    # print()

    # for h in range(height+2):
    #     print(open_door_table2[h])
    # print()
 
    # for h in range(height+2):
    #     print(open_door_table3[h])

    answer = int(1e9)
    for h in range(height):
         for w, (val1, val2, val3) in enumerate(zip(open_door_table1[h], open_door_table2[h], open_door_table3[h])):
             if val1 == -1 or val2 == -1 or val3 == -1:
                 continue
 
             if _map[h][w] == "*":
                 continue
             
             elif _map[h][w] == ".":
                 answer = min(answer, val1 + val2 + val3)
 
             elif _map[h][w] == "#":
                 answer = min(answer, val1 + val2 + val3 - 2)

    print(answer)