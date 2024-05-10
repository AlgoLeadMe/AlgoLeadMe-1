import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []
for i in range(n):
    ground.append(list(map(int, input().split())))

answer = int(1e9)
idx = 0

for floor in range(257):
    # task1 -> 블록을 빼는 것
    # task2 -> 블록을 추가하는 것
    task1 = 0
    task2 = 0
    for x in range(n):
        for y in range(m):
            # 블록이 층수보다 크면
            if ground[x][y] > floor:
                task1 += ground[x][y] - floor 
            # 블록이 층수보다 작으면
            else:
                task2 += floor - ground[x][y]
    
    # 블록을 추가하는 것 > 가지고 있던 블록의 합 + 블록을 빼서 가져온 것이면 
    # 블록을 더 못가져오는데 가져왔으므로 다시 처음으로
    if task2 > task1 + b:
        continue
    # 시간 초를 구하고 최저 시간과 비교
    count = task1 * 2 + task2
    if count <= answer:
        answer = count
        idx = floor

print(answer, idx)