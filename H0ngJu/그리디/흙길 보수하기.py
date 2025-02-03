import sys
import math

def input(): return sys.stdin.readline().strip()
N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort()

prev_start = -1
prev_end = -1
cnt = 0

for start, end in info:
    if prev_end < end:
        if start <= prev_end:
            prev_start = prev_end + 1
        else:
            prev_start = start
        need = math.ceil((end - prev_start) / L)
        prev_end = need * L + prev_start - 1
        cnt += need

print(cnt)