from collections import defaultdict

def sm(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def solution(target):
    # 필요 다트 수, -(싱글 또는 불을 맞춘 횟수)
    memo = defaultdict(lambda : [987654321, 987654321])
    memo[0] = [0, 0]
    memo[50] = [1, -1]
    
    # 싱글, 더블, 트리플 저장
    for point in range(1, 21):
        memo[point] = [1, -1]
        memo[point * 2] = min(memo[point * 2], [1, 0])
        memo[point * 3] = min(memo[point * 3], [1, 0])
    
    # 59까지 바텀업
    for i in range(21, 60):
        for j in range(1, i):
            memo[i] = min(memo[i], sm(memo[i - j], memo[j]))
    
    answer = [987654321, 987654321]
    
    # 50을 0~5번 넣는다.
    for i in range(6):
        tempTarget = target
        tempTarget -= 50 * i
        if (tempTarget < 0): break
        tempAnswer = [i, -i]
        tempAnswer[0] += tempTarget // 60
        tempTarget %= 60
        tempAnswer = sm(tempAnswer, memo[tempTarget])
        answer = min(answer, tempAnswer)
    
    answer[1] *= -1
    return answer