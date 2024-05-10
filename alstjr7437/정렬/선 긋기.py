import sys
input = sys.stdin.readline

n = int(input())
dohwaji = [tuple(map(int,(input().split()))) for _ in range(n)]

# for i in range(len(dohwaji)):
#     dohwaji[i][0] += 1000000000
#     dohwaji[i][1] += 1000000000

dohwaji.sort()

line = dohwaji[0][1]
answer = dohwaji[0][1] - dohwaji[0][0]

for left, right in dohwaji[1:]:
    if right <= line:
        continue
    elif line < left:
        answer += right - left
        line = right
    elif line >= left and right > line: 
        answer += right - line
        line = right
    # print(answer)

print(answer)