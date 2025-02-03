import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
info = [list(map(int, input().split())) + [i] for i in range(N)]
dp = [0 for _ in range(N)]
answer = [0 for _ in range(N)]

# 완탐 -> 시간 초과
# a가 b보다 크면 (색이 다르다는 가정 하에), a는 b 값을 + 하면 됨 -> 누적합 -> 전체 값에서 같은 색만 빼주기

info.sort(key=lambda x: (x[1], x[0]))
total = 0
color_sum = [0 for _ in range(200001)]
size_sum = [0 for _ in range(200001)]
pre_size = 0 # 다른 컬러이면서 같은 사이즈인 경우를 위해 저장
pre_color = 0

for i in range(N):
    color, size, index = info[i]

    if pre_color == color and pre_size == size:
        dp[index] = dp[info[i-1][2]]
    else : 
        dp[index] = total - color_sum[color] - size_sum[size]
    
    total += size
    color_sum[color] += size # 같은 색깔의 합
    size_sum[size] += size # 같은 사이즈의 합

    pre_size = size
    pre_color = color

for i in dp:
    print(i)

# 예외 케이스
# 3
# 1 4
# 2 4
# 1 4

# 6  
# 1 5
# 2 6
# 7 6
# 5 6
# 2 6
# 1 6

# 5
# 3 15
# 3 15
# 3 5
# 1 15
# 2 10