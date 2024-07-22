import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

DP = [[-float('inf')] * M for _ in range(N)]
DP[0][0] = board[0][0]

# 첫 번째 행 초기화
for j in range(1, M):
    DP[0][j] = DP[0][j-1] + board[0][j]

# 각 행 처리
for i in range(1, N):
    left_to_right = [-float('inf')] * M
    right_to_left = [-float('inf')] * M

    # 현재 행에서 왼쪽에서 오른쪽으로 탐색
    left_to_right[0] = DP[i-1][0] + board[i][0]
    for j in range(1, M):
        left_to_right[j] = max(DP[i-1][j], left_to_right[j-1]) + board[i][j]

    # 현재 행에서 오른쪽에서 왼쪽으로 탐색
    right_to_left[M-1] = DP[i-1][M-1] + board[i][M-1]
    for j in range(M-2, -1, -1):
        right_to_left[j] = max(DP[i-1][j], right_to_left[j+1]) + board[i][j]

    # 결과 병합
    for j in range(M):
        DP[i][j] = max(left_to_right[j], right_to_left[j])

print(DP[N-1][M-1])
