import sys
sys.setrecursionlimit(10**6)

def input(): return sys.stdin.readline().rstrip()

S = list(input())
T = list(input())

def solution(cur, target):
    if len(cur) == len(target): # len(cur) == len(target)
        if cur == target:
            return 1
        else: return 0
    
    elif len(cur) < len(target): # len(cur) < len(target)
        if target[-1] ==  "A":
            target.pop()
            return solution(cur, target)
        else:
            target.pop()
            target = target[::-1]
            return solution(cur, target)

    else: # len(cur) > len(target)
        return 0

print(solution(S, T))