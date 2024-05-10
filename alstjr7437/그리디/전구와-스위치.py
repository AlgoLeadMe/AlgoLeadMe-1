def solution(first, target, count):
    # 첫번째 버튼을 누른 경우 처리
    if count == 1:
        first[0] = 1 - first[0]
        first[1] = 1 - first[1]
    # 버튼 순회
    for i in range(1,n):
        if first[i-1] == target[i-1]:   # 바꿔야하는지 비교
            continue
        count += 1
        for j in range(i-1, i+2):   # 1번이면 0~2번까지 전구 바꾸기
            if j < n:   # n이 3일때 3을 누르면 2,3만 되도록
                first[j] = 1 - first[j]
    if first == target:
        return count
    else :
        return -1
    
n = int(input())
first = list(map(int, input()))
target = list(map(int, input()))

# 첫번째 전구의 스위치를 누르는 경우
result1 = solution(first[:], target, 1)
# 첫번째 전구의 스위치를 누르지 않는 경우
result2 = solution(first[:], target, 0)

if result1 == -1:
    print(result2)
elif result2 == -1:
    print(result1)
else : 
    print(min(result1, result2))