import sys

def input(): return sys.stdin.readline()
INF = int(1e9)

visited = set()
N = int(input())
indegree = [[0,set()] for _ in range(N+1)]
receipe = [[] for _ in range(N+1)]
outdegree = [[] for _ in range(N+1)]
answer = [INF for _ in range(N+1)]
can_build = []

for idx in range(1,N+1):
    _input = list(map(int,input().split()))
    indegree[idx][0] = _input[0]
    receipe[idx] = _input[1:-1]
    indegree[idx][1] = set(_input[1:-1])
    for out in _input[1:-1]:
        outdegree[out].append(idx)
    
    if len(indegree[idx][1]) == 0:
        can_build.append(idx)
        visited.add(idx)
        answer[idx] = _input[0]

while can_build:
    now = can_build.pop()

    for next_building in outdegree[now]:
        indegree[next_building][1].discard(now)
        
        if len(indegree[next_building][1]) == 0 and next_building not in visited:
            can_build.append(next_building)
            
            max_temp = -1
            for ingredient in receipe[next_building]:
                max_temp = max(max_temp, answer[ingredient])
                
            answer[next_building] = min(answer[next_building], max_temp + indegree[next_building][0])
            visited.add(next_building)
            
for ans in answer[1:]:
    print(ans)