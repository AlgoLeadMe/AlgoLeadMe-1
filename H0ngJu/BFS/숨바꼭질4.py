import sys
from collections import deque

def input(): return sys.stdin.readline()

N, K = map(int, input().split())

visited = [0] * 100001
time = 0
parent = [-1] * 100001

q = deque([N])
visited[N] = 1

while q:
    size = len(q)
    for _ in range(size):
        location = q.popleft()
        if location == K: 
            print(time)
            answer = []
            while location != -1:
                answer.append(location)
                location = parent[location]
            answer.reverse()
            print(" ".join(map(str, answer)))
            break
        for next_location in (location + 1, location - 1, location * 2):
            if 0 <= next_location <= 100000 and not visited[next_location]:
                q.append(next_location)
                visited[next_location] = 1
                parent[next_location] = location
    time += 1
