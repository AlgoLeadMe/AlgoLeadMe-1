cnt=0
def DFS(virus):
    global cnt
    visited[virus]=1

    for i in network[virus]:
        if (visited[i]==0):
            DFS(i)
            cnt+=1

N= int(input())
link = int(input())

network = [[]*(N+1) for _ in range(N+1)]
for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
visited = [0]*(N+1)
DFS(1)
print(cnt)
