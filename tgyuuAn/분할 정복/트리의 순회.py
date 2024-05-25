import sys

sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

N = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
position = [0 for _ in range(N+1)]

for idx, element in enumerate(in_order):
    position[element] = idx
    
def divide_and_conquer(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end: return

    in_order_root = post_order[post_end]
    print(in_order_root, end=" ")
    
    root_idx = position[in_order_root]
    
    divide_and_conquer(in_start, root_idx-1, post_start, post_start+(root_idx - in_start) -1)
    divide_and_conquer(root_idx+1, in_end, post_start+(root_idx - in_start), post_end-1)
    
    return

divide_and_conquer(0, N-1, 0, N-1)