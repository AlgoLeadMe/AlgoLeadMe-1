from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

_input = input()

def check(string, mid):
    temp = defaultdict(int)
    for start_idx in range(len(string)-mid+1):
        now = string[start_idx:start_idx+mid]
        temp[now] += 1
        if temp[now] >=2 : return True
    return False

answer = 0
left = 0
right = len(_input)
while left+1 < right:
    mid = (left+right)//2
    
    # 만약 해당 버퍼 크기에 답이 있다면
    if check(_input, mid):
        answer = mid
        left = mid
    else: right = mid
    
print(answer)