def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            idx = stack.pop()
            answer[idx] = n
        stack.append(i)

    return answer