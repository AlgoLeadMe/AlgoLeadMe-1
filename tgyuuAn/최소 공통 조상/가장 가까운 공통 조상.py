import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N+1)]
    
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A

    x, y = map(int, input().split())
    x_depth = 0
    now_node = x
    while now_node != 0:
        now_node = parent[now_node]
        x_depth += 1

    y_depth = 0
    now_node = y
    while now_node != 0:
        now_node = parent[now_node]
        y_depth += 1

    while x_depth > y_depth:
        x_depth -= 1
        x = parent[x]

    while y_depth > x_depth:
        y_depth -= 1
        y = parent[y]

    while x != y:
        x = parent[x]
        y = parent[y]

    print(x)