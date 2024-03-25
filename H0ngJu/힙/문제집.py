import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
q = []
answer = []

# 입력받아서 넣기
for _ in range(m):
    p1, p2 = map(int, sys.stdin.readline().rstrip().split())
    graph[p1].append(p2) # p1은 p2와 연결된 문제
    inDegree[p2] += 1 # 간선 추가

# 진입차수가 0이면 큐에 넣기
for i in range(1, n+1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

# answer에 넣고, 간선 제거
while q:
    prob = heapq.heappop(q)
    answer.append(prob)
    for i in graph[prob]: # 간선 제거 & 진입차수 0인 것들 처리
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

for result in answer:
    print(result, end=" ")