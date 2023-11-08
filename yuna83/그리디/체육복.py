def solution(n, lost, reserve):
    
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
            
    return n - len(new_lost)