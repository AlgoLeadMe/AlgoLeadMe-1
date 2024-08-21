from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

def command(register, cmd):
    if cmd == 0:
        return ((register * 2) % 10000, "D")
    elif cmd == 1:
        return (9999 if register == 0 else register - 1, "S")
    elif cmd == 2:
        return (register % 1000 * 10 + register // 1000, "L")
    elif cmd == 3:
        return (register // 10 + (register % 10) * 1000, "R")

for _ in range(T):
    A, B = map(int, input().split())

    visited = [False] * 10000
    visited[A] = True

    queue = deque([(A, "")])
    while queue:
        cur, result = queue.popleft()
        
        if cur == B:
            print(result)
            break
        
        for i in range(4):
            register, cmd = command(cur, i)
            if not visited[register]:
                visited[register] = True
                queue.append((register, result + cmd))