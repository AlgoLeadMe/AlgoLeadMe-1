from copy import deepcopy

def solution(r, c, sy, sx, queries):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    yRange = [sy, sy]
    xRange = [sx, sx]
    
    for dir, dist in queries[::-1]:
        # 모서리에 박지 않았을 경우 이동
        if not(dir == 0 and xRange[0] == 0):
            xRange[0] -= dx[dir] * dist
        if not(dir == 1 and xRange[1] == c - 1):
            xRange[1] -= dx[dir] * dist
        if not(dir == 2 and yRange[0] == 0):
            yRange[0] -= dy[dir] * dist
        if not(dir == 3 and yRange[1] == r - 1):
            yRange[1] -= dy[dir] * dist
        
        if not (0 <= yRange[0] < r) and not (0 <= yRange[1] < r): return 0
        if not (0 <= xRange[0] < c) and not (0 <= xRange[1] < c): return 0
        if yRange[0] > yRange[1] or xRange[0] > xRange[1]: return 0
        
        # 범위 정규화
        yRange[0] = max(0, min(r - 1, yRange[0]))
        yRange[1] = max(0, min(r - 1, yRange[1]))
        xRange[0] = max(0, min(c - 1, xRange[0]))
        xRange[1] = max(0, min(c - 1, xRange[1]))
    
    return (yRange[1] - yRange[0] + 1) * (xRange[1] - xRange[0] + 1)