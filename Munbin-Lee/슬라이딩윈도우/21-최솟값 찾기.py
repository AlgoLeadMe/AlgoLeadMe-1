from collections import deque

stdin = open(0)
N, L = map(int, stdin.readline().split())
A = tuple(map(int, stdin.readline().split()))
deq = deque()
answer = []

for k, v in enumerate(A):
    while deq and deq[-1][1] >= int(v): deq.pop()
    if deq and deq[0][0] + L <= k: deq.popleft()
    deq.append((k, v))
    answer.append(deq[0][1])

print(' '.join(map(str, answer)))