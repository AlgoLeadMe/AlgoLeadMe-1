from sys import *

N = int(stdin.readline())
K = int(stdin.readline())
SENSORS = sorted(set(map(int, stdin.readline().split())))

if K >= N:
    print(0)
    exit()

distances = [SENSORS[i] - SENSORS[i - 1] for i in range(1, len(SENSORS))]
distances.sort(reverse=True)

result = 0
for i in range(K - 1, len(distances)):
    result += distances[i]

print(result)
