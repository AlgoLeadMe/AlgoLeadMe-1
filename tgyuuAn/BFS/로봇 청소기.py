from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while True:
    column, row = map(int,input().split())

    if (column, row) == (0,0):
        break
    
    board = []
    target = []
    start = [(0,0)]

    for r in range(row):
        _input = list(input())
        
        for c, i in enumerate(_input):
            if i == "o":
                start = [(c, r)]
                continue

            if i == "*":
                target.append((c,r))
                continue

        board.append(_input)

    # print(board)
    # print(target, start)

    table = [[int(1e9) for _ in range(len(target)+1)] for _ in range(len(target)+1)]

    for prev_idx, (x,y) in enumerate(start+target):
        
        deq = deque([[x,y,0]])
        visited = set((x,y))

        while deq:
            now = deq.popleft()

            for dir in range(4):
                new_x = now[0] + dx[dir]
                new_y = now[1] + dy[dir]

                if new_x <0 or new_x >= column:
                    continue

                if new_y <0 or new_y >= row:
                    continue

                if (new_x, new_y) in visited:
                    continue

                if board[new_y][new_x] == "x":
                    continue
                
                else:
                    if board[new_y][new_x] == "*":
                        
                        for next_idx, (target_x, target_y) in enumerate(target):
                            if (target_x, target_y) == (new_x, new_y):
                                table[prev_idx][next_idx+1] = now[2] + 1
                                break

                    deq.append([new_x, new_y, now[2]+1])
                    visited.add((new_x,new_y))

    min_cost = int(1e9)
    visited = [False for _ in range(len(table))]

    def dfs(visited, table, now, cost, depth):
        global min_cost
        # print(depth, visited)

        if depth == len(visited)-1:
            min_cost = min(min_cost, cost)
            return
        
        for idx, now_cost in enumerate(table[now]):
            if idx == 0 or idx == now: continue

            if visited[idx] == True: continue 

            visited[idx] = True
            dfs(visited, table, idx, cost+now_cost, depth+1)
            visited[idx] = False
        
    for start_idx, start_cost in enumerate(table[0]):
        if start_idx == 0: continue

        visited[start_idx] = True
        dfs(visited, table, start_idx, start_cost, 1)
        visited[start_idx] = False
    
    if min_cost == int(1e9): print(-1)
    else: print(min_cost)