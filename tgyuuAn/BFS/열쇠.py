import sys 
from collections import deque, defaultdict

def input(): return sys.stdin.readline().rstrip()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for _ in range(T):

    H, W = map(int, input().split())
    building = [["." for _ in range(W+2)]]
    door_info = defaultdict(set)
    keys_i_have = set()

    for row in range(H):
        _input = "."
        _input += input()
        _input += "."

        for col in range(W+2):
            if _input[col] not in ("*", ".", "$") and _input[col].isupper():
                door_info[_input[col]].add((row+1, col))
                
        building.append(list(_input))

    building.append(["." for _ in range(W+2)])
    
    keys_info = input()
    if keys_info != "0":
        keys_i_have.update(set(keys_info))
    
    answer = 0
    visited = set()
    locked_doors_to_access = set()
    
    deq = deque([(0, 0)])
    while deq:
        now_row, now_col = deq.popleft()
        
        for dir in range(4):
            new_row = now_row + dy[dir]
            new_col = now_col + dx[dir]
            
            if new_row < 0 or new_row >= H+2: continue
            if new_col < 0 or new_col >= W+2: continue
            if (new_row, new_col) in visited: continue
            if building[new_row][new_col] == "*": continue
            
            # print(now_row, now_col,building[new_row][new_col])
            # print(locked_doors_to_access)
            # print(keys_i_have)
            # print()
            
            if building[new_row][new_col] == "$":
                answer += 1
                visited.add((new_row, new_col))
                deq.append((new_row, new_col))
                continue
            
            # 문을 만났을 경우, 이 때 까지 얻은 열쇠로 열 수 있는 지 확인함. 아닐 경우 접근할 수 있는 문 목록에 추가
            if building[new_row][new_col].isalpha() and building[new_row][new_col].isupper():

                # 열쇠를 이미 가지고 있는 경우
                if building[new_row][new_col].lower() in keys_i_have:
                    building[new_row][new_col] = "."
                    visited.add((new_row, new_col))
                    deq.append((new_row, new_col))
                    
                # 열쇠가 없어서 문을 못 열 경우 접근할 수 있는 문 목록에 추가
                else: locked_doors_to_access.add((new_row, new_col))
                
                continue
            
            # 열쇠를 획득했을 경우, 이 때 까지 만난 문들 중에 열 수 있는 것들을 queue에 넣음
            if building[new_row][new_col].isalpha() and building[new_row][new_col].islower():
                keys_i_have.add(building[new_row][new_col])
                visited.add((new_row, new_col))
                deq.append((new_row, new_col))
                
                for can_open_row, can_open_col in door_info[building[new_row][new_col].upper()]:
                    if (can_open_row, can_open_col) in locked_doors_to_access:
                        building[can_open_row][can_open_col] = "."
                        visited.add((can_open_row, can_open_col))
                        deq.append((can_open_row, can_open_col))
                        locked_doors_to_access.discard((can_open_row, can_open_col))
                        
                continue
            
            # 빈 공간일 경우, 그냥 지나감
            if building[new_row][new_col] == ".":
                visited.add((new_row, new_col))
                deq.append((new_row, new_col))
                
    print(answer)