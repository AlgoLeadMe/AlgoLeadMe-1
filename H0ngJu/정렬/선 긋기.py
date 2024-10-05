import sys

def input() : return sys.stdin.readline().rstrip()

length = 0
start = 0
end = 0

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

for i in range(N):
    x, y = lines[i]
    if i == 0:
        start = x
        end = y
    else:
        if x<= end:
            end = max(end, y)
        else:
            length += abs(end-start) # 이전 선분은 필요 없음
            start = x
            end = y

print(abs(end-start + length))