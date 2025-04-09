import sys
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

N = int(input())
strings = list()
board = defaultdict(int)
can_not_be_zero = set()

for _ in range(N):
    string = input()
    strings.append(string)
    can_not_be_zero.add(string[0])
    
    for idx, string in enumerate(string[-1::-1]):
        board[string] += 10**(idx)

answer = defaultdict(int)

is_zero = ""
if len(board) >= 10:
    for (key, value) in sorted(list(board.items()), key = lambda x : x[1]):
        if key in can_not_be_zero: continue
    
        is_zero = key
        answer[key] = "0"
        break

now = 9
for (key, value) in sorted(list(board.items()), key = lambda x : x[1], reverse = True):
    if key == is_zero: continue
        
    answer[key] = str(now)
    now -= 1
    
accum = 0
for string in strings:
    accum += int("".join(map(lambda x : answer[x], string)))

print(accum)