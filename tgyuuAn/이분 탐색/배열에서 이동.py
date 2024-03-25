from collections import deque

array_length = int(input())
board = [list(map(int,input().split())) for _ in range(array_length)]

min_value = int(1e9)
max_value = -1

for row in board:
    for col in row:
        min_value = min(min_value, col)
        max_value = max(max_value, col)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def check(mid):
    # print(mid,"일 때는  통과하나 ?")

    # (0부터 0+mid) 까지를 (200-mid부터 200) 까지 체크
    for _min in range(min_value,max_value-mid+1):
        _max = _min + mid
        
        visited = set()
        deq = deque()
        # 시작 지점이 _min ~ _max 범위를 벗어나면 건너뜀
        if board[0][0] < _min or board[0][0] > _max:
            continue
        
        deq.append([0,0])
        visited.add((0,0))
        while deq:
            now_x, now_y = deq.popleft()

            if (now_x, now_y) == (array_length-1, array_length-1):
                # print("응")
                return True
            
            for direction in range(4):
                new_x = now_x + dx[direction]
                new_y = now_y + dy[direction]

                if new_x < 0 or new_x >= array_length:
                    continue
                
                if new_y < 0 or new_y >= array_length:
                    continue

                if (new_x, new_y) in visited:
                    continue

                if board[new_y][new_x] < _min or board[new_y][new_x] > _max:
                    continue
                
                visited.add((new_x, new_y))
                deq.append([new_x,new_y])

    # print("아니")
    # 모든 경우를 탐색해도 도저히 끝에 도달할 수 없는 경우 False를 반환
    return False

left = -1
right = max_value - min_value + 1
answer = 0
while left + 1 < right:
    mid = (left + right) // 2
    # print(left, mid, right)
    
    if check(mid):
        answer = mid
        right = mid
    else:
        left = mid
        
print(answer)