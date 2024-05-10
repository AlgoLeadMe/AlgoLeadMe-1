from collections import deque
import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]
r, c = map(int, input().split())

water1 = deque()
water2 = deque()
visited = [[False] * c for _ in range(r)]

swan1 = deque()
swan2 = deque()
visited2 = [[False] * c for _ in range(r)]

# 1. 전체 호수 만들기
river = []
for i in range(r):
    river.append(list(input()))

day_count = 0

# 2. 백조 위치 찾기와 물 위치 찾기
swan = []
for x in range(c):
    for y in range(r):
        if river[y][x] == "L":
            swan.append([y,x])
            river[y][x] = "."
        if river[y][x] == ".":
            water1.append([y, x])
            visited[y][x] = True

# 3. 백조를 큐에 추가 
swan1.append(swan[0])
visited2[swan[0][0]][swan[0][1]] = True

# 4. 하루에 한번씩 X 없애기(얼음 없애기)
def break_ice():
    # print("-------")
    while water1:
        y, x = water1.popleft()
        # print(y, x, water1, water2)
        river[y][x] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if not visited[ny][nx]:
                if river[ny][nx] == ".":
                    water1.append([ny,nx])
                else :
                    water2.append([ny,nx])
                visited[ny][nx] = True
                
# 5. 백조가 만나는지 체크하기
def check_swan():
    # print("-------")
    while swan1 : 
        y, x = swan1.popleft()
        # print(x,y,swan1, swan2)
        if y == swan[1][0] and x == swan[1][1]:
            print(day_count)
            sys.exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if not visited2[ny][nx]:
                if river[ny][nx] == "." and visited2[ny][nx] == False:
                    swan1.append([ny,nx])
                else :
                    swan2.append([ny,nx])
                visited2[ny][nx] = True
    return False

# 만날때까지 돌리기
while 1:
    break_ice()
    water1 = water2
    water2 = deque()

    check_swan()
    swan1 = swan2
    swan2 = deque()
    day_count += 1