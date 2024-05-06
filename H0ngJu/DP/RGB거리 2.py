import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
INF = 1000*1000+1

house = [[int(x) for x in input().split()] for _ in range(N)]
cost = INF

for first_house in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][first_house] = house[0][first_house]  
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1] 
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
    dp[N-1][first_house] = INF
    cost = min(cost, min(dp[N-1]))

print(cost)