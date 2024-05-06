import sys
from collections import *

def input(): return sys.stdin.readline().strip()
N = int(input())

arr = list(map(int, input().split()))
arr.reverse()
answer = [-1 for _ in range(N)]

id = 0

stack = []
stack.append((id,arr.pop()))

while arr:
    id += 1
    arr_data = arr.pop()
    while stack and stack[-1][1] < arr_data:
        index, data = stack.pop()
        answer[index] = arr_data
    stack.append((id, arr_data))

for i in answer:
    print(i, end=" ")