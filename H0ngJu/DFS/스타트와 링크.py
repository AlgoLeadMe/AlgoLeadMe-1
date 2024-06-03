import sys

def input() : return sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = 999999999
 
def solution(len, idx):
    global answer
    
    if len == N//2:
        link = 0
        start = 0

        for i in range (N):
            for j in range (N):
                if visited[i] and visited[j]: # 방문한 반만 팀
                    start += arr[i][j]
                elif not visited[i] and not visited[j]: # 나머지 반 팀
                    link += arr[i][j]
        
        answer = min(answer, abs(start-link))
        return
    
    else: # 인원 나누기
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = 1
                solution(len+1, i+1)
                visited[i] = 0
 
solution(0,0)
print(answer)