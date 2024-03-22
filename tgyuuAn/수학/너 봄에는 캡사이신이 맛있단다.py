import sys

DIV = 1_000_000_007

def input(): return sys.stdin.readline().rstrip()

def power(n, over):
    if over == 0: return 1
    elif over == 1: return n
    elif over %2 == 0: 
        half = (power(n, over//2) % DIV)
        return (half * half) % DIV
    else: 
        half = (power(n, over//2) % DIV)
        return (half * half * (n % DIV)) % DIV

N = int(input())
numbers = sorted(list(map(int,input().split())))
DP = [-1 for _ in range(N)]
answer = 0

for start_idx in range(N):
    start_num = numbers[start_idx]
    end_num = numbers[N-start_idx-1]

    # 만약 캐싱이 되어있지 않을 경우 직접 계산
    if DP[N-start_idx-1] == -1: DP[N-start_idx-1] = power(2, N-start_idx-1)
    
    # 한번이라도 계산  했으면 바로 이용
    answer += ((end_num % DIV) * (DP[N-start_idx-1] % DIV)) % DIV
    answer -= ((start_num % DIV) * (DP[N-start_idx-1] % DIV)) % DIV

print(answer % DIV)