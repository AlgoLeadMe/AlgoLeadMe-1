import sys
sys.setrecursionlimit(10 ** 6)

def input(): return sys.stdin.readline().rstrip()

N = int(input())
# N = 30 만 -> O(N*log(N))

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

answer = 0
def dfs(now_idx, visited, tree):
    global answer
    
    temp_cnt = 1
    for next_node in tree[now_idx]:
        if next_node in visited: continue
        visited.add(next_node)
        temp = dfs(next_node, visited, tree)
        answer += temp * (temp-1) // 2
        answer += temp * (N-temp)
        temp_cnt += temp

    return temp_cnt

dfs(1,{1,}, tree)
print(answer)    
