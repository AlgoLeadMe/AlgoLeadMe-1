def solution(r1, r2):
    return find_interger_coordinates_include_boundary(r2) - find_interger_coordinates_exclude_boundary(r1)

def find_interger_coordinates_include_boundary(radious):
    
    count = 0
    #y값을 r부터 1까지 탐색
    for y in range(radious,0,-1):
        
        max_x = int(pow((radious**2 - y**2), 0.5))
        count += max_x*2 + 1
        
    count *= 2
    count += radious * 2 + 1
    
    return count

def find_interger_coordinates_exclude_boundary(radious):
    
    count = 0
    #y값을 r부터 1까지 탐색
    for y in range(radious,0,-1):
        
        #경계를 포함하지 않으므로, y = 반지름인 부분은 포함하지 않음
        if y == radious:
            continue
        
        if pow((radious**2 - y**2), 0.5) == int(pow((radious**2 - y**2), 0.5)):
            max_x = pow((radious**2 - y**2), 0.5) - 1
            count += (max_x*2 + 1)
            continue
        
        max_x = int(pow((radious**2 - y**2), 0.5))
        count += max_x*2 + 1
        
    count *= 2
    count += (radious-1) * 2 + 1
    
    return count