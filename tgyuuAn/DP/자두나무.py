import sys

def input(): return sys.stdin.readline()

T, W = map(int,input().split())

# DP[i][j][k] i초에 [j]위치에 있고 [k]번의 횟수를 이동했을 때 받을 수 있는 자두 수
DP = [[[0 for _ in range(W+1)] for _ in range(2+1)] for _ in range(T+1)]

plums = []
for _ in range(T):
    plums.append(int(input()))

for time, plum in zip(range(1,T+1), plums):

    for k in range(W+1):
        if k == 0:
            if plum == 1:
                DP[time][1][k] = DP[time-1][1][k]+1
                DP[time][2][k] = DP[time-1][2][k]

            else:
                DP[time][1][k] = DP[time-1][1][k]
                DP[time][2][k] = DP[time-1][2][k]+1 
            continue

        if plum == 1:
            DP[time][1][k] = max(DP[time-1][1][k],DP[time-1][2][k-1])+1
            DP[time][2][k] = max(DP[time-1][1][k-1],DP[time-1][2][k])

        else:
            DP[time][1][k] = max(DP[time-1][1][k],DP[time-1][2][k-1])
            DP[time][2][k] = max(DP[time-1][1][k-1],DP[time-1][2][k])+1

    DP[time][2][0] = 0

print(max([max(x) for x in DP[-1]]))