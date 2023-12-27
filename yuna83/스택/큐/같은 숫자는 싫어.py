from collections import deque

def solution(arr):
    answer = []
    queue = deque()

    for num in arr:
        if queue and queue[-1] == num:
            continue
        else:
            queue.append(num)
 
    answer = list(queue)

    return answer