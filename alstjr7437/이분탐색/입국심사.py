def solution(n, times):
    answer = 0
    # left = 제일 작은 시간, right = 제일 많은 시간
    left = min(times)
    right = max(times) * n
    while left <= right :
        mid = (right + left) // 2
        people = 0      # 심사 가능 인원 수 담기
        # 심사 가능한 사람 수 게산을 위한 반복문
        for i in times:     
            people += mid // i 
            # 모든 심사관을 거치지 않아도 n명 이상의 심사를 할 수 있으면 탈출
            if people >= n:
                break
        # 심사 사람 수가 받아야할 사람 수(n) 보다 많으면 왼쪽 범위
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사 사람 수가 받아야할 사람 수(n) 보다 적으면 오른쪽 범위
        else :
            left = mid + 1
    return answer