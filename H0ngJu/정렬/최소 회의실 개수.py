import sys
import heapq

def input() : return sys.stdin.readline().rstrip()

N = int(input()) # 100000
info = [tuple(map(int, input().split())) for _ in range(N)]
room = []

info.sort(key=lambda x: x[0])
heapq.heappush(room, info[0][1])
answer = 1

for i in range(1,N):
    a, b = info[i][0], info[i][1]
    if a >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, b)

print(len(room))