from collections import deque

TOP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction_mapper = {TOP : "TOP", DOWN : "DOWN", LEFT : "LEFT", RIGHT : "RIGHT"}

dx = [0,0,-1,1]
dy = [-1,1,0,0]

class Node:
    def __init__(self,direction,y,x):
        self.direction = direction
        self.y = y
        self.x = x
        #상, 하, 좌, 우로 들어올 때 False를 True로 변경
        self.incoming_direction_flag = [False, False, False, False]
        
    def __str__(self):
        return f"{self.direction} {self.x} {self.y} {self.incoming_direction_flag})"
    
    def shoot(self,incoming_direction):

        #만약, 위쪽에서 온 레이저 일 경우,
        if incoming_direction == TOP:

            #내가 직진으로 보내는 노드라면
            if self.direction == "S":

                #그 다음 노드가 받는 incoming_direction 또한 TOP일 것임
                shoot_direction = TOP
                

            #내가 왼쪽으로 꺾어 보내는 노드라면
            elif self.direction == "L":

                #그 다음 노드가 받는 incoming_direction은 LEFT일 것이다.
                shoot_direction = LEFT


            #내가 오른쪽으로 꺾어 보내는 노드라면
            elif self.direction == "R":
                
                #그 다음 노드가 받는 incoming_direction은 RIGHT일 것이다.
                shoot_direction = RIGHT
            
        elif incoming_direction == DOWN:
        
            if self.direction == "S":
                shoot_direction = DOWN

            elif self.direction == "L":
                shoot_direction = RIGHT

            elif self.direction == "R":
                shoot_direction = LEFT
        
        elif incoming_direction == LEFT:
            
            if self.direction == "S":
                shoot_direction = LEFT

            elif self.direction == "L":
                shoot_direction = DOWN

            elif self.direction == "R":
                shoot_direction = TOP

        elif incoming_direction == RIGHT:
            
            if self.direction == "S":
                shoot_direction = RIGHT

            elif self.direction == "L":
                shoot_direction = TOP

            elif self.direction == "R":
                shoot_direction = DOWN        
        
        return shoot_direction

def solution(grid):
    
    ##노드 초기화
    total_node = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_x_len = len(grid[0])
    total_y_len = len(grid)
    answer = []
    
    for idx_row, rows in enumerate(grid):
        for idx_col, direction in enumerate(rows):
            total_node[idx_row][idx_col] = Node(direction,idx_row, idx_col)
    
    ##각 노드 순회(완전 탐색)
    for rows in total_node:
        for node in rows:
            
            for idx, is_can_incoming in enumerate(node.incoming_direction_flag):
                
                if is_can_incoming == False:
                    deq = deque()
                    deq.append([node.y,node.x,idx])
                    node.incoming_direction_flag[idx] = True
                    count = 1

                    while deq:
                        now = deq.popleft()
                        now_y, now_x = now[0], now[1]
                        now_node = total_node[now_y][now_x]
                        incoming_direction = now[2]
                        shoot_direction = now_node.shoot(incoming_direction)

                        new_x = now_x + dx[shoot_direction]
                        new_y = now_y + dy[shoot_direction]
                        new_x = (new_x + total_x_len) % total_x_len
                        new_y = (new_y + total_y_len) % total_y_len
                        
                        new_node = total_node[new_y][new_x]
                        if new_node.incoming_direction_flag[shoot_direction] == False:
                            new_node.incoming_direction_flag[shoot_direction] = True
                            deq.append([new_y, new_x, shoot_direction])
                            count += 1

                        else:
                            break

                    answer.append(count)
        
    return sorted(answer)