from collections import *

def solution(text):
    if len(text) % 2 == 1:
        return 0

    non_pairs = deque()
    for char in text:
        if len(non_pairs) > 0 and non_pairs[-1] == char:
            non_pairs.pop()
        else:
            non_pairs.append(char)
    
    return int(len(non_pairs) == 0)