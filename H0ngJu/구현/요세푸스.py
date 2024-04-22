import sys

def input(): 
    return sys.stdin.readline().rstrip()

def solution(k):
    location = 0
    cnt = 0

    while table:
        if cnt == k - 1:
            answer.append(table.pop(location))
            location -= 1 # 삭제한 경우에는 위치를 앞으로 이동
            cnt = 0
        else:
            cnt += 1
        if len(table) != 0:
            location = (location + 1) % len(table)

    return answer

n, k = map(int, input().split())
table = [i + 1 for i in range(n)]
answer = []

solution(k)
print("<" + ", ".join(map(str, answer)) + ">")