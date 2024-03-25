def check(mid, stones, k):
    gap = 0
    for stone in stones:
        if stone - mid < 0: gap += 1
        else: gap = 0

        if gap >= k: return False
    return True
    
def solution(stones, k):
    left = -1
    right = 200000001
    answer = 0
    
    while left+1<right:
        mid = (left+right)//2
        
        if check(mid, stones, k): # mid 명이 건널 수 있을 경우 건너는 수를 더 늘림
            left = mid
            answer = mid
            
        else:
            right = mid
            
    return answer
