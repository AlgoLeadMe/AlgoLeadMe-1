from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, k) for k, i in enumerate(priorities)]) # 튜플 큐 생성
    priorities.sort(reverse=True) # 내림차순 정렬
    
    while queue:
        cur = queue.popleft() # 가장 앞의 프로세스 꺼내기 (queue.pop(0)) 
        if cur[0] == priorities[0]: # 내림차순으로 정렬된 우선순위 == 현재 순위 -> 가장 높음
            answer += 1 # 수 ++
            if cur[1] == location: # 찾고자하는 process인 경우
                break
            priorities.pop(0)
        else:
            queue.append(cur) # 뒤로 미루기

    return answer

#test