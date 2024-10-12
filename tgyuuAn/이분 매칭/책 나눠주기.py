import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    matches_n = [0 for _ in range(N+1)]
    matches_m = [0 for _ in range(M+1)]
    want = dict()

    for idx in range(1,M+1):
        a, b = map(int, input().split())
        want[idx] = [idx for idx in range(a, b+1)]

    def dfs(now, graph, visited):
        visited[now] = True
    
        for _next in graph[now]:
            if matches_n[_next] == 0:
                matches_n[_next] = now
                matches_m[now] = _next
                return True
        
            elif visited[matches_n[_next]] == False and dfs(matches_n[_next], graph, visited):
                matches_m[now] = _next
                return True
            
        return False
    
    answer = 0
    for i in range(1,M+1):
        visited = [False for _ in range(M+1)]
        if(dfs(i, want, visited)):
            answer += 1
        
    print(answer)