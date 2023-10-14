import copy
from collections import deque

def solution(A,B):
    # idxs = [e for e in range(len(A))]
    # a_idxs = set(idxs)
    # b_idxs = set(idxs)
    return sortAndFind(A,B)

def sortAndFind(A,B):
    a = sorted(A)
    b = sorted(B,reverse=True)
    total = 0

    for i in range(len(A)):
        total += (a[i] * b[i])
    
    return total

####################
def findRecursive(a, b, a_idxs, b_idxs, total_sum):
    if len(b_idxs) == 0:
        return total_sum
    
    consumed_a = []
    min_sum = 999999999
    
    for ai in a_idxs:
        if a[ai] in consumed_a:
            continue

        new_a_idxs = copy.deepcopy(a_idxs)
        new_a_idxs.remove(ai)
        sums = []
        consumed_b = []
        
        for bi in b_idxs:
            if b[bi] in consumed_b:
                continue
                
            new_b_idxs = copy.deepcopy(b_idxs)
            new_b_idxs.remove(bi)
            sums.append(find(a, b, new_a_idxs, new_b_idxs, total_sum + a[ai] * b[bi]))
            consumed_b.append(b[bi])
        
        consumed_a.append(a[ai])
        min_sum = min(min_sum, min(sums))
    return min_sum