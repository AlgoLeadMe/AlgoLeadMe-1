from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    return bfs(maps, n, m, visited)

def bfs(maps, n, m, visited):
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
   
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
   
    while queue:
        x, y, distance = queue.popleft()
       
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
                     
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                if (nx, ny) == (n - 1, m - 1):
                    return distance + 1  
                   
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
   
    return -1 