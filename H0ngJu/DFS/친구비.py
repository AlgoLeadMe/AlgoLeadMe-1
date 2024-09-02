import sys
from collections import deque, defaultdict

def input() : return sys.stdin.readline().rstrip()

N, M, k = map(int, input().split())
friend_money = list(map(int, input().split()))
relation = defaultdict(set)
visited = [0] * N
total = 0

for _ in range(M):
    a, b = map(int, input().split())
    relation[a-1].add(b-1)
    relation[b-1].add(a-1)

for i in range(N):
    if not visited[i]:
        visited[i] = True
        friends = []
        q = deque([i])
        
        while q:
            f = q.popleft()
            friends.append(f)
            for p in relation[f]:
                if not visited[p]:
                    visited[p] = True
                    q.append(p)

        if friends:
            cost = min(friend_money[friend] for friend in friends)
            total += cost

if total <= k:
    print(total)
else:
    print("Oh no")
