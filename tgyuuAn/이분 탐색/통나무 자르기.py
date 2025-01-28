import sys

def input(): return sys.stdin.readline().rstrip()

L, K, C = map(int, input().split())
cut_points = sorted(list(map(int, input().split())))
cut_points = [0] + cut_points + [L]

def check(max_len):
    cuts = 0
    last_cut = L
    for i in range(len(cut_points) - 1, 0, -1):
        if cut_points[i] - cut_points[i - 1] > max_len:
            return False
        if last_cut - cut_points[i - 1] > max_len:
            cuts += 1
            last_cut = cut_points[i]
    return cuts <= C

left, right = 1, L
answer = L
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

cuts = 0
last_cut = L
first_cut = None
for i in range(len(cut_points) - 1, 0, -1):
    if last_cut - cut_points[i - 1] > answer:
        cuts += 1
        last_cut = cut_points[i]
        if C == cuts:
            first_cut = cut_points[i]

if first_cut is None:
    first_cut = cut_points[1]

print(answer, first_cut)