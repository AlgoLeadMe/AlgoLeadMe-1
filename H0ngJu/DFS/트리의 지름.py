import sys
sys.setrecursionlimit(10**9)
def input() : return sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
visited[1] = 0

for i in range(n-1):
    v, u, w = map(int, input().split())
    tree[v].append((u, w))
    tree[u].append((v, w))

def dfs(start, dis):
    for node, node_dis in tree[start]:
        if visited[node] == -1:
            visited[node] = dis + node_dis
            dfs(node, dis + node_dis)

dfs(1,0)

far_node = visited.index(max(visited))
visited = [-1] * (n+1)
visited[far_node] = 0
dfs(far_node, 0)

print(max(visited))