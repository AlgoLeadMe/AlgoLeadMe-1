import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())
info = [[]]
for i in range(N):
    people = list(map(int, input().split()))
    info.append(people[:-1])
M = int(input()) # 최초 유포자 수
rumor = list(map(int, input().split()))

answer = [-1] * (N+1)
belive = [0] * (N+1)
time = 0
q = deque()

for r in rumor: # 최초 유포자
    q.append([r, 0])
    answer[r] = 0

while q:
    person, time = q.popleft()
    
    cnt = 0
    for p in info[person]:
        if p == 0:
            break
        if answer[p] == -1:
            belive[p] += 1
            
            if belive[p] >= (len(info[p]) + 1) // 2:
                answer[p] = time + 1
                q.append((p, time+1))   

print(*answer[1:])