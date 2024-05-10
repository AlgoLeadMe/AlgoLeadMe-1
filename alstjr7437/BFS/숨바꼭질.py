from collections import deque

n, k = map(int, input().split())

result = [0] * 100001
result[n] = 1

queue = deque()
queue.append(n)

while queue:
    now = queue.popleft()
    if now == k:
        break
    # -1 로직
    if now - 1 >= 0 and result[now-1] == 0 :
        queue.append(now-1)
        result[now-1] = result[now] + 1
    # +1 로직
    if now + 1 < len(result) and result[now+1] == 0:
        queue.append(now+1)
        result[now+1] = result[now] + 1
    # *2 로직
    if now * 2 < len(result) and result[now * 2] == 0:
        queue.append(now*2)
        result[now*2] = result[now] + 1

print(result[k] - 1)