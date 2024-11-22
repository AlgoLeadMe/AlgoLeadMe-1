import sys

def input() : return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

left = max(lecture)
right = sum(lecture)

while left <= right:
    mid = (left+right)//2
    record_cnt = 1
    time = 0 # 레코드 하나에 들어가는 시간

    for i in range(N):
        if time + lecture[i] > mid: # 시간 초과되면 다음 레코드로
            record_cnt += 1
            time = lecture[i]
        else:
            time += lecture[i]

    if record_cnt <= M: # 깅의가 남아있으면 크기 줄이기
        right = mid - 1
    else:
        left = mid + 1

print(left)