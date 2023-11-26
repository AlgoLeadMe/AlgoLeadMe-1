from collections import *

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    
    count = 0
    weight_sum = people.popleft()
    
    while people:
        if weight_sum + people[-1] <= limit:
            people.pop()
            
        weight_sum = people.popleft() if people else 0
        count += 1
    
    if weight_sum:
        count += 1
        
    return count