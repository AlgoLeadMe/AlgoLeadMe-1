n, k = map(int, input().split())

weight = []
values = []

for i in range(n):
    a, b = map(int, input().split())
    weight.append(a)
    values.append(b)

dp = [0] * (k+1)

for i in range(n):
    for j in range(k,-1,-1):
        if j-weight[i] >= 0:
            dp[j] = max(dp[j], dp[j-weight[i]] + values[i])

print(max(dp))