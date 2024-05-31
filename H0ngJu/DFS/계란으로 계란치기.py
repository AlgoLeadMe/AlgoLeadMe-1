import sys
sys.setrecursionlimit(10**6)

def input(): return sys.stdin.readline().rstrip()

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

def break_egg(idx):
    cnt = 0
    
    # idx가 넘어간 경우
    if idx == N:
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1
        return cnt

    if eggs[idx][0] <= 0: # 들고 있는 계란이 깨진 경우
        return break_egg(idx+1)
    
    broken = False
    for j in range(N): # 계란 깨기
        if j != idx and eggs[j][0] > 0:
            broken = True
            eggs[idx][0] -= eggs[j][1]
            eggs[j][0] -= eggs[idx][1]

            cnt = max(cnt, break_egg(idx+1))

            eggs[idx][0] += eggs[j][1]
            eggs[j][0] += eggs[idx][1]

    if not broken:
        return break_egg(idx+1)
    
    return cnt

print(break_egg(0))
