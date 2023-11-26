from collections import *

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    
    count = 0
    weight = people.popleft()
    
    while people:
        if weight + people[-1] <= limit:
            people.pop()
            
        weight = people.popleft() if people else 0
        count += 1
    
    if weight:
        count += 1
        
    return count