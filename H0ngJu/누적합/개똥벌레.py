import sys

def input() : return sys.stdin.readline().rstrip()

N, H = map(int, input().split())
# N <= 200000, H<= 500000
# 석순, 종유석, 석순, 종유석 ...
up = [0 for _ in range(H+1)]
down = [0 for _ in range(H+1)]
min_broke = 1e9
broke_cnt = 0

for i in range(N):
    info_h = int(input())
    if i % 2 == 0:
        down[info_h] += 1
    else:
        up[info_h] += 1

for i in range(H-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, H+1):
    broke = up[i] + down[H-i+1]
    if broke < min_broke:
        min_broke = broke
        broke_cnt = 1
    elif broke == min_broke:
        broke_cnt += 1

print(min_broke, broke_cnt)

