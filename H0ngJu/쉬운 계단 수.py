import sys

DIV = 1_000_000_000

N = int(sys.stdin.readline().rstrip())

dp = [[0] * 10 for _ in range(N+1)] 
answer = 0

for i in range(1,N+1):
    if i == 1:
        for k in range(1,10):
            dp[i][k] = 1
    
    else:
        for num in range(10):
            if num == 0:
                dp[i][num] = dp[i-1][1]%DIV
            elif num == 9:
                dp[i][num] = dp[i-1][8]%DIV
            else:
                dp[i][num] = (dp[i-1][num-1] + dp[i-1][num+1])%DIV

for k in range(10):
    answer += dp[N][k]

print(answer%DIV)

