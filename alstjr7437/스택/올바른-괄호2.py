"""
백준 올바른 괄호 문제
"""

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else :
            if stack :
                stack.pop()
            else :
                return False
    if stack :
        return False
    return True

num = int(input())
for i in range(num):
    s = input()
    print("YES" if solution(s) else "NO")