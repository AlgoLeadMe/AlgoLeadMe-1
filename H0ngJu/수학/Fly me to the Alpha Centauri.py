import sys

def input() : return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0

    for _ in range(distance+1):
        if distance <= cnt**2:
            break
        else:
            cnt += 1
    
    if distance <= (cnt-1)*cnt:
        print((cnt-1)*2)
    else:
        print(cnt*2-1)