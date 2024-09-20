import sys

INF = 1e8

def input() : return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
bus = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    A, B, C = map(int, input().split())
    bus[A].append([B, C])

def BellmanFord(start):
    distance[start] = 0
    
    for i in range(N):
        for j in range(1, N+1):
            for n, w in bus[j]:
                if distance[j] != INF and distance[n] > distance[j] + w:
                    distance[n] = distance[j] + w
                    if i == N-1:
                        return True
    return False

check_negative = BellmanFord(1)

if check_negative:
    print("-1")
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])
