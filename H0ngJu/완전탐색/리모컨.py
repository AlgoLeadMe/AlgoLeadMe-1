import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
btn = list(map(int, input().rsplit()))

target = abs(N-100)
cnt = target

for i in range(1000001):
    check = True
    for str_i in str(i):
        if int(str_i) in btn:
            check = False
            break

    if check:
        cnt = min(cnt, abs(i - N)+len(str(i)))

print(cnt)