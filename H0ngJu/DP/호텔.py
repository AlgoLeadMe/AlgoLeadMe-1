import sys

def input(): return sys.stdin.readline().rstrip()

C, N = map(int, input().split()) # C < 1000 N <= 20
info = [list(map(int, input().split())) for _ in range(N)]
max_p = 0
for i in range(N):
    max_p = max(max_p, info[i][1])
idx = C+max_p+1

dp = [1e9] * idx
dp[0] = 0

for value, person in info:
    for i in range(person, idx):
        dp[i] = min(dp[i-person]+value, dp[i])

print(min(dp[C:]))