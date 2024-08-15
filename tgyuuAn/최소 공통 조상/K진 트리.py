import sys

def input(): return sys.stdin.readline().rstrip()

N, K, Q = map(int,input().split())

for _ in range(Q):
    start, dest = map(int, input().split())
    answer = 0

    if K == 1:
        print(abs(start - dest))
        continue
        
    while start != dest:
        if start > dest:
            start = (start-2)//K+1
            answer += 1

        if dest > start:
            dest = (dest-2)//K+1
            answer += 1
    
    print(answer)