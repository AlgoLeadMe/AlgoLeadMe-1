import sys

def input(): return sys.stdin.readline().rstrip()

M = int(input())
f_x = list(map(int, input().split()))

# 희소 배열 초기화
table = [[0] * (M + 1) for _ in range(30)]
table[0] = [0] + f_x  # 첫 번째 레벨 초기화

# 희소 배열 채우기
for i in range(1, 30):  # 2^i 단계를 계산
    for x in range(1, M + 1):
        table[i][x] = table[i - 1][table[i - 1][x]]

# 쿼리 처리
Q = int(input())
for _ in range(Q):
    N, X = map(int, input().split())
    # N을 이진수로 표현해 필요한 단계만 수행
    for i in range(30):
        if N & (1 << i):  # i번째 비트가 1이라면
            X = table[i][X]
    print(X)
