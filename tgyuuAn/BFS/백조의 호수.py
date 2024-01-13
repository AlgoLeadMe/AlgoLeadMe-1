from collections import deque

row, col = map(int,input().split())

lake = [[None for _ in range(col)] for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
swans = []
swan_moving_point = deque()
water = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for r in range(row):
    element_col = list(input())
    for element, c in zip(element_col,range(col)):
        lake[r][c] = element
        
        if lake[r][c] == "L":
            swans.append((r,c))

        if lake[r][c] in (".", "L"):
            water.append((r,c))

visited[swans[0][0]][swans[0][1]] = True
swan_moving_point.append((swans[0][0],swans[0][1]))

def melt_ice(water, lake):
    next_water = deque()

    while water:
        water_r, water_c = water.popleft()

        for water_dir in range(4):
            new_water_r, new_water_c = water_r + dy[water_dir], water_c + dx[water_dir]

            if not (0 <= new_water_r < row):
                continue

            if not (0 <= new_water_c < col):
                continue

            if lake[new_water_r][new_water_c] == "X":
                next_water.append((new_water_r,new_water_c))
                lake[new_water_r][new_water_c] = "."

    return next_water

def find_swan(swan_moving_point,lake):
    next_swan_moving_point = deque()

    while swan_moving_point:
        swan_r, swan_c = swan_moving_point.popleft()

        for swan_dir in range(4):
            new_swan_r, new_swan_c = swan_r + dy[swan_dir], swan_c + dx[swan_dir]

            if not (0 <= new_swan_r < row):
                continue

            if not (0 <= new_swan_c < col):
                continue

            if visited[new_swan_r][new_swan_c] == True:
                continue

            visited[new_swan_r][new_swan_c] = True

            if lake[new_swan_r][new_swan_c] == ".":
                swan_moving_point.append((new_swan_r,new_swan_c))
                
            if lake[new_swan_r][new_swan_c] == "X":
                next_swan_moving_point.append((new_swan_r,new_swan_c))
            
            if lake[new_swan_r][new_swan_c] == "L":
                return None, True

    return next_swan_moving_point, False

days = 0
while True:
    water = melt_ice(water,lake)
    swan_moving_point, isFindFriend = find_swan(swan_moving_point,lake)

    if isFindFriend:
        print(days+1)
        break

    days += 1