from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    temp_reverse = False
    error = 0

    p = input()
    n = int(input())
    x = deque(input().strip()[1:-1].split(','))

    if n == 0 :
        x = deque()
        
    for i in p:
        if i == 'R':
            if temp_reverse :
                temp_reverse = False
            else :
                temp_reverse = True

        if i == "D":
            if len(x) == 0:
                error = 1
                break
            else :
                if temp_reverse :
                    x.pop()
                else :
                    x.popleft()
    
    if temp_reverse :
        x.reverse()

    if error == 0 :
        print(f"[{','.join(str(i) for i in x)}]")
    else : 
        print("error")
