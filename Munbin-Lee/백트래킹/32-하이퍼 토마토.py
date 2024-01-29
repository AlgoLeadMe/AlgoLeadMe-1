from math import prod
from collections import deque

stdin = open(0)
sizes = list(map(int, stdin.readline().split()))
totalSize = prod(sizes)
board = []
unripe = 0
index = 0
deq = deque()

for line in stdin.read().splitlines():
    for num in map(int, line.split()):
        board.append(num)
        
        if num == 0:
            unripe += 1
        
        if num == 1:
            deq.append(index)
        
        index += 1

if unripe == 0:
    print('0')
    exit()

def extract(x):
    answer = [0] * 11
    divisor = totalSize
    
    for i in range(10, -1, -1):
        divisor //= sizes[i]
        answer[i] = x // divisor
        x %= divisor
    
    return answer

def compress(ls):
    answer = 0
    coefficient = 1
    
    for i in range(0, 11):
        answer += ls[i] * coefficient
        coefficient *= sizes[i]
    
    return answer

while deq:
    cur = deq.popleft()
    positions = extract(cur)
    
    for i in range(0, 11):
        for offset in (-1, 1):
            positions[i] += offset
            
            if 0 <= positions[i] < sizes[i]:
                next = compress(positions)
            
                if board[next] == 0:
                    board[next] = board[cur] + 1
                    unripe -= 1
                    deq.append(next)
            
            positions[i] -= offset
        
        if unripe == 0:
            print(board[cur])
            exit()

print('-1')