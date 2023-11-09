def solution(k, m, score): #k:최고점, m:갯수
    answer = 0
    score = sorted(score, reverse = True)
    
    for i in range(0,len(score),m):
        box = score[i:i+m] 
        if len(box) == m:
            answer += min(box)*m
            
    return answer