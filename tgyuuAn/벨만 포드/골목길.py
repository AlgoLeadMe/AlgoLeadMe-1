import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]

# 간선 정보 받음
for _ in range(M):
    start, destination, cost = map(int,input().split())
    edge[start].append([destination, cost])

# 초기 세팅
board = [-int(1e9) for _ in range(N+1)]
board[1] = 0

# 최적의 경로를 찾기 위해 역추적 하기 위해서 이전 노드를 기록
prev_node = [-1 for _ in range(N+1)]
prev_node[1] = 0

for _ in range(N-1):
    for start in range(1,N+1):
        for destination, cost in edge[start]:
            if board[destination] < board[start] + cost:
                board[destination] = board[start] + cost
                prev_node[destination] = start

has_cycle = False
is_connect_target = False
for start in range(1,N+1):
    for destination, cost in edge[start]:
        # 사이클 발생
        if board[destination] < board[start] + cost:
            has_cycle = True

            # 사이클이 발생해도 경로랑 관련이 없을 수도 있으므로,
            # 사이클이 발생한 지점이 목표 지점과 관련이 있는지 체크크
            deq = deque([start])
            visited = {start,}
            while deq:
                now = deq.popleft()

                for d, c in edge[now]:
                    if d in visited: continue

                    deq.append(d)
                    visited.add(d)

                    # 사이클이 있고 목표지점 혹은 시작지점과 붙어있으면 -1
                    if d == 1 or d == N:
                        is_connect_target = True
                        break

                if is_connect_target: break
            break

# 사이클이 있는데 해당 사이클이 목표와 연결되어 있을 경우
if has_cycle and is_connect_target: print(-1)
else:
    answer = []
    now = N
    while now != 1:
        answer.append(now)
        now = prev_node[now]

    answer.append(now)

    if now != 1: print(-1)
    else: print(*answer[::-1])

# 총 간선 = 2만개,
# 총 노드 = 100개
# 벨만 포드 = ( 간선 X 노드 -1 ) -> 198만 시간 복잡도 가능.

# 최적의 경로
# 사이클이 발생해도 갈 수 있을 수 있음.
# 사이클이 없더라도 도달할 수 없을 수 있음.