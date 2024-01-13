direction_board = {
    0 : [[0,-0.5],[0,-1]],
    1 : [[0.5,-0.5],[1,-1]],
    2 : [[0.5,0],[1,0]],
    3 : [[0.5,0.5],[1,1]],
    4 : [[0,0.5],[0,1]],
    5 : [[-0.5,0.5],[-1,1]],
    6 : [[-0.5,0],[-1,0]],
    7 : [[-0.5,-0.5],[-1,-1]],
}

def solution(arrows):
    answer = 0
    now_x, now_y = 0,0
    visited = {(0,0)}
    visited_path = set()
    
    for arrow in arrows:
        check_path, real_path = direction_board[arrow]
        
        check_x, check_y = now_x + check_path[0], now_y + check_path[1]
        real_x, real_y = now_x + real_path[0], now_y + real_path[1]
        
#        print(real_x,real_y)
#        print(visited_path)
#        print(visited)
        
        #대각선 교차할 때 먼저 체크
        if arrow in [1,7,5,3]:
            if(check_x, check_y) in visited:
                if ((now_x,now_y),(real_x,real_y)) not in visited_path:
                    answer += 1
                
        if (real_x, real_y) in visited:
            if ((now_x,now_y),(real_x,real_y)) not in visited_path:
                answer += 1                
                
        visited.add((real_x, real_y))
        visited.add((check_x, check_y))
        visited_path.add(((now_x, now_y), (real_x, real_y)))
        visited_path.add(((real_x, real_y),(now_x, now_y)))
        now_x, now_y = real_x, real_y
#        print(answer)
#        print()
        
    return answer