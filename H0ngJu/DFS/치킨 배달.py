import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
house = [[] for _ in range(N)]
chicken_house = []
chicken_dis = [[9999 for _ in range(N)] for _ in range(N)]
result = 99999

for i in range(N):
    house[i].extend(map(int, input().split()))

for r in range(N):
    for c in range(N):
        if house[r][c] == 2:
            chicken_house.append((r, c))

for chickens in combinations(chicken_house, M):
    total = 0
    for r in range(N):
        for c in range(N):
            if house[r][c] == 1:
                tmp = 9999
                for chicken in chickens:
                    tmp = min(tmp, abs(r - chicken[0]) + abs(c - chicken[1]))
                total += tmp
    
    result = min(result, total)

print(result)