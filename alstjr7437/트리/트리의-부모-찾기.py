import sys
sys.setrecursionlimit(10**8) #재귀 리미트
from collections import deque

n = int(input())

# 트리 만들기
tree = {i:[] for i in range(1,n+1)}
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)

# 부모 저장하기
visited = [0] * (n+1)

# DFS
def dfs(a):
    for i in tree[a]:
        if visited[i] == 0:
            visited[i] = a
            # print(visited, i, a)
            dfs(i)

# BFS
def bfs():
    while queue:
        a = queue.popleft()
        for i in tree[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = a
                # print(visited, queue)


visited[1] = '어무이'

# dfs(1)

queue = deque()
queue.append(1)
bfs()

for i in range(2, n+1):
    print(visited[i])