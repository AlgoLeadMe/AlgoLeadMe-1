import sys

def input() : return sys.stdin.readline().rstrip()

N = int(input()) # 100000
info = [tuple(map(int, input().split())) for _ in range(N)]


info.sort(key=lambda x: (x[1], x[0]))
# 최대한 많이 넣으려면 빨리 끝나는 회의들을 정렬을 해야함
# ** 끝나는 시간이 같은 경우를 고려해야함 **

tmp_a,tmp_b  = info[0][0], info[0][1]
answer = 1

for i in range(1,N):
    a = info[i][0]
    b = info[i][1]

    if a >= tmp_b:
        tmp_a, tmp_b = a, b
        answer += 1

print(answer)