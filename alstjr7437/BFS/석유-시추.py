from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, visited, land, result):
    count = 0
    visited[x][y] = 1
    q = deque()
    q.append([x,y])
    min_y, max_y = y, y
    while q:
        x,y = q.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                continue
                
            if visited[nx][ny] == 0 and land[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx,ny])
                
    for i in range(min_y, max_y+1):
        result[i] += count

def solution(land):
    result = [0] * len(land[0])
    visited = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, visited, land, result)
                
    print(result)
    return max(result)