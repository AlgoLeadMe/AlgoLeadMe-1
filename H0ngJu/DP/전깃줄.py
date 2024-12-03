import sys

def input() : return sys.stdin.readline().rstrip()

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

info.sort()

LIS = [1] * N

for i in range(1, N):
    for j in range(i):
        if info[j][1] < info[i][1]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

print(N-max(LIS))