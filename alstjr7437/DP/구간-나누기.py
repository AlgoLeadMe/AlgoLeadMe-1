# n, m = map(int,input())

# num = [ i for i in range(n): int(input())]

# dp = [[-1e9] * m for _ in range(n+1)]
# for i in range(n):

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp1 = [[0]+[-1e9]*m for i in range(n+1)]
dp2 = [[0]+[-1e9]*m for i in range(n+1)]
num = [int(input()) for i in range(n) ]

for i in range(1, n+1):
    for j in range(1, min(m, (i+1)//2)+1):
        dp2[i][j]=max(dp1[i-1][j], dp2[i-1][j])
        dp1[i][j]=max(dp1[i-1][j], dp2[i-1][j-1])+num[i-1]
print(max(dp1[n][m], dp2[n][m]))

