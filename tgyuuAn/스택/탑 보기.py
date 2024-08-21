import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
building = list(map(int,input().split()))
answer_count = [0 for _ in range(N)]
answer_idx = [int(1e9) for _ in range(N)]
stack = []
for idx in range(N-1,-1,-1):
    now_height = building[idx]
    if len(stack) == 0: stack.append((now_height, idx))
    else:
        while stack and now_height >= stack[-1][0]:
            stack.pop()

        if len(stack) > 0:
            if answer_idx[idx] != int(1e9) and abs(answer_idx[idx]-idx) < abs(stack[-1][1] - idx): 
                stack.append((now_height, idx))
                continue

            answer_idx[idx] = stack[-1][1]
            answer_count[idx] += len(stack)

        stack.append((now_height, idx))
        
stack = []            
for idx in range(N):
    now_height = building[idx]
    if len(stack) == 0: stack.append((now_height, idx))
    else:
        while stack and now_height >= stack[-1][0]:
            stack.pop()
            
        if len(stack) > 0:
            if answer_idx[idx] != int(1e9) and abs(answer_idx[idx]-idx) < abs(stack[-1][1] - idx): 
                answer_count[idx] += len(stack)
                stack.append((now_height, idx))
                continue
            
            answer_idx[idx] = stack[-1][1]
            answer_count[idx] += len(stack)
        
        if stack and stack[-1][0] == now_height: continue
        
        stack.append((now_height, idx))

for count, idx in zip(answer_count, answer_idx):
    if idx == int(1e9): print(0)
    else: print(count, idx+1)