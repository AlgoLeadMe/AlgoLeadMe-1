import sys

def input() : return sys.stdin.readline().rstrip()

wheels = [list(int(r) for r in input()) for _ in range(4)]
score = 0

K = int(input())
cmds = [list(map(int, input().split())) for _ in range(K)]

def leftshift(arr):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = tmp

def rightshift(arr):
    tmp = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = tmp
        

for n, cmd in cmds:
    n -= 1
    left_check = [False] * 4
    right_check = [False] * 4

    if cmd == 1:
        right_check[n] = True
    else:
        left_check[n] = True

    for i in range(n, 0, -1):
        if wheels[i][6] != wheels[i-1][2]:
            if left_check[i]:
                right_check[i-1] = True
            if right_check[i]:
                left_check[i-1] = True
        else:
            break
    
    for i in range(n,3):
        if wheels[i][2] != wheels[i+1][6]:
            if left_check[i]:
                right_check[i+1] = True
            if right_check[i]:
                left_check[i+1] = True
        else:
            break

    for i in range(4):
        if left_check[i]:
            leftshift(wheels[i])
        
        if right_check[i]:
            rightshift(wheels[i])
    

for i in range(4):
    if wheels[i][0] == 1:
        score += 2**i

print(score)