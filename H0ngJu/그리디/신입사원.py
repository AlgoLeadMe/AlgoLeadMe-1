import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    apply = [list(map(int, input().split())) for _ in range(N)]
    apply = sorted(apply)
    top = 0
    cnt = 1

    for i in range(1, N):
        if apply[i][1] < apply[top][1]:
            top = i
            cnt += 1
    
    print(cnt)