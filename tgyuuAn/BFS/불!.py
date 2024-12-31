import sys

def input(): return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
start = (0, 0)
fire = []

## 보드를 만드는데, 가장자리를 도착 지점(*)으로 감싼다.
board = [["*" for _ in range(C+2)]]
for r in range(R):
    _input = input()
    row = ["*"]
    for c, elem in enumerate(_input):
        if elem == "J": start = (r+1, c+1)
        elif elem == "F": fire.append((r+1, c+1))
        row.append(elem)
    row.append("*")
    board.append(row)
board.append(["*" for _ in range(C+2)])

# for x in board: print(x)
# 불이 퍼지는 위치를 먼저 계산한 후, 지훈이가 갈 수 있는 위치를 계산 함.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

f = fire[:]
f_visited = set(fire)

j = [start]
j_visited = {start,}

answer = 1
answer_flag = False
while j:
    temp_f = []
    while f:
        (now_r, now_c) = f.pop()
        
        for dire in range(4):
            new_r = now_r + dy[dire]
            new_c = now_c + dx[dire]
            
            if new_r < 0 or new_r >= R+2: continue
            if new_c < 0 or new_c >= C+2: continue
            if board[new_r][new_c] == "#": continue
            if board[new_r][new_c] == "*": continue
            if (new_r, new_c) in f_visited: continue
        
            temp_f.append((new_r, new_c))
            f_visited.add((new_r, new_c))
            
    temp_j = []
    
    while j:
        (now_r, now_c) = j.pop()
        
        for dire in range(4):
            new_r = now_r + dy[dire]
            new_c = now_c + dx[dire]
            
            if new_r < 0 or new_r >= R+2: continue
            if new_c < 0 or new_c >= C+2: continue
            if board[new_r][new_c] == "#": continue
            if (new_r, new_c) in j_visited: continue
            if (new_r, new_c) in f_visited: continue
        
            if board[new_r][new_c] == "*":
                answer_flag = True
                print(answer)
                break
                
        
            temp_j.append((new_r, new_c))
            j_visited.add((new_r, new_c))
    
        if answer_flag: break
    if answer_flag: break
    f = temp_f[:]
    j = temp_j[:]
    answer += 1
    
else: print("IMPOSSIBLE")