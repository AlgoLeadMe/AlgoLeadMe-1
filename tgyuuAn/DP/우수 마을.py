import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def input(): return sys.stdin.readline().rstrip()

N = int(input())
town = [0]
town.extend(list(map(int,input().split())))
linked = defaultdict(set)

for _ in range(N-1):
    first, second = map(int,input().split())

    linked[first].add(second)
    linked[second].add(first)

DP = [[0, town[n]] for n in range(N+1)]
visited = set()

def dfs(now):
    visited.add(now)
    
    for next in linked[now]:   
        if next not in visited:
            dfs(next)
            DP[now][1] += DP[next][0]  
            DP[now][0] += max(DP[next][0], DP[next][1])  

dfs(1)
print(max(DP[1][1], DP[1][0]))