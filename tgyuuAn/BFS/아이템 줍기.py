from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    table = [[0 for _ in range(101)] for _ in range(101)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = set()
    in_rectangle = set()
    
    for l_b_x, l_b_y, r_t_x, r_t_y in rectangle:
        for x in range(l_b_x*2, r_t_x*2+1):
            table[l_b_y*2][x] = 1
            table[r_t_y*2][x] = 1
            
        for y in range(l_b_y*2, r_t_y*2+1):
            table[y][l_b_x*2] = 1
            table[y][r_t_x*2] = 1
        
        for x in range(l_b_x*2+1, r_t_x*2):
            for y in range(l_b_y*2+1, r_t_y*2):
                in_rectangle.add((x,y))
                
    # 아이템이 있는 위치를 9로 설정.
    table[itemY*2][itemX*2] = 9
    
    #for row in table[-1::-1]:
    #    print(row)
        
    deq = deque()
    deq.append([characterX*2, characterY*2, 0])
    visited.add((characterX*2, characterY*2))
    while deq:
        now_x, now_y, distance = deq.popleft()
        
        for direction in range(4):
            new_x = now_x + dx[direction]
            new_y = now_y + dy[direction]
            
            if new_x > 100 or new_x < 0:
                continue
            
            if new_y > 100 or new_y < 0:
                continue
            
            if table[new_y][new_x] == 0:
                continue
                
            if table[new_y][new_x] == 9:
                return distance + 0.5
            
            if table[new_y][new_x] == 1:
                if (new_x, new_y) not in visited and (new_x, new_y) not in in_rectangle:
                    visited.add((new_x, new_y))
                    deq.append([new_x, new_y, distance+0.5])
    
    return