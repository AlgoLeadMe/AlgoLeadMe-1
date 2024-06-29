import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    k = x  # k를 x로 초기화
    result = -1  
    while k <= m * n:  # k의 범위는 m*n을 넘을 수 없게
        if (k - x) % m == 0 and (k - y) % n == 0: 
            result = k  
            break  
        k += m 

    print(result)  # 결과값 출력