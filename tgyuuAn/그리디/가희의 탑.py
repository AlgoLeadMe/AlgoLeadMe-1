import sys

def input(): return sys.stdin.readline().rstrip()

N, a, b = map(int, input().split())
if(N+1<(a+b)): print(-1)
else:
    answer = [0 for _ in range(N)]
    
    if a>b:
        for idx, element in enumerate(range(N-a-b+1, N-b+1)):
            answer[element] = idx+1
        
        for idx, element in enumerate(range(N-1, N-b, -1)):
            answer[element] = idx+1
        
        for idx in range(N-a-b+1):
            answer[idx] = 1
        
    else:   
        for idx, element in enumerate(range(N-b, N)):
            answer[element] = b - idx

        for idx, element in enumerate(range(N-b-a+1, N-b)):
            answer[element] = idx+1

        for idx in range(N-b-a+1):
            answer[idx] = 1
             
        if a == 1:
            answer[N-b], answer[0] = answer[0], answer[N-b]
            
    print(*answer)