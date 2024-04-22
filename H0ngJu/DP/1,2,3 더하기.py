import sys

def input(): return sys.stdin.readline().strip()

T = int(input())

answer = []
dp = [0] * (11)

for index in range(T):
    data = int(input())

    for i in range(1, data + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    answer.append(dp[data])

for a in answer:
    print(a, end=" ")