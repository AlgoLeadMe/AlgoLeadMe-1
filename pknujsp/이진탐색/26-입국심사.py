def solution(n, times):
    times.sort()  # 현재 문제의 모든 테스트 케이스 입력은 정렬되어 들어옵니다
    left, right = 1, times[-1] * n

    while left < right:
        mid = (left + right) // 2
        count = 0

        for time in times:
            count += mid // time

        if count < n:
            left = mid + 1
        else:
            right = mid

    return left
