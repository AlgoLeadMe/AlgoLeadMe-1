def dfs(n, cnt):
    global ans
    # 가지치기: 이대로 진행해도 정답 갱신 가능성 없는 경우 더 이상 진행 X
    if ans >= (cnt+(L+1-n)//2):    # 남은 자리 다 놓아도 정답 갱신 안되는 경우
        return

    if n>=L:
        ans = max(ans, cnt)
        return

    for ci,cj in lst[n]:    # 현재 사선번호에서 가능한 위치 하나씩 놓고 다음 사선으로..
        if v[ci-cj]==0:
            v[ci-cj]=1
            dfs(n+2, cnt+1)
            v[ci-cj]=0
    dfs(n+2, cnt)           # 이번 사선에서 안놓고 다음사선으로..

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [[] for _ in range(2*N)]
# arr[i][j]==1인경우 i+j 위치에 append
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            lst[i+j].append((i,j))
L = 2*N-1
v = [0]*(2*N)

# 체스판의 흑/백은 비숍이 상호간 이동 불가!
# 0부터 시작해서 2씩증가 + 1부터 시작해서 2씩증가
ans = 0
dfs(0, 0)   # 0부터 2씩 증가
t = ans
ans = 0
dfs(1, 0)   # 1부터 2씩 증가
print(ans+t)