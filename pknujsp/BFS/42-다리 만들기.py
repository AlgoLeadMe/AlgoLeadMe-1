from collections import *

map_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(map_size)]

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
island_id = 2
costs = [[0] * map_size for _ in range(map_size)]

# 다리를 놓을 위치를 저장할 큐
bridge_queue = deque()

# 전체 맵을 순회하면서 각 섬에 ID 부여
for row in range(map_size):
    for col in range(map_size):
        
        if matrix[row][col] != 1:
            continue
            
        # 현재 칸을 시작으로 하는 섬에 고유 ID 할당
        matrix[row][col] = island_id
        queue = deque([(row, col)])
        
        # BFS를 통해 같은 섬인 육지에 ID 할당
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not 0 <= nr < map_size or not 0 <= nc < map_size:
                    continue
                    
                # 다른 섬과 연결된 바다 영역에 접근하면 종료
                if 1 < matrix[nr][nc] < island_id:
                    print(1)
                    exit()
                    
                # 새로운 육지 발견 시 큐에 추가
                if matrix[nr][nc] == 1:
                    queue.append((nr, nc))
                # 육지와 바로 맞닿은 바다 영역을 다리 후보로 추가
                elif matrix[nr][nc] == costs[nr][nc] == 0:
                    bridge_queue.append((nr, nc, 1, island_id))
                    
                costs[nr][nc] = 1
                matrix[nr][nc] = island_id
                
        island_id += 1

min_cost = int(1e6)

# 다리 후보 위치를 순회하며 최소 다리 길이 계산
while bridge_queue:
    r, c, cost, curr_island_id = bridge_queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if not 0 <= nr < map_size or not 0 <= nc < map_size:
            continue
            
        # 아직 다리가 놓이지 않은 바다 영역이면
        # 다리 길이를 증가시키고 큐에 추가
        if costs[nr][nc] == 0:
            bridge_queue.append((nr, nc, cost + 1, curr_island_id))
            
            costs[nr][nc] = cost + 1
            matrix[nr][nc] = curr_island_id
        # 다른 섬과 연결된 다리 영역에 접근하였다면 최소 비용을 갱신
        elif matrix[nr][nc] > 1 and matrix[nr][nc] != curr_island_id:
            min_cost = min(min_cost, cost + costs[nr][nc])

print(min_cost)