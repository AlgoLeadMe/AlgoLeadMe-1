from collections import *
from sys import *

stdin = open("7569.txt", "r")

RIPE, UNRIPE = 1, 0

C, R, Z = map(int, stdin.readline().split())
rows = R * Z

box = [list(map(int, stdin.readline().split())) for _ in range(rows)]
q = deque()

for r, row in enumerate(box):
    for c in range(C):
        if row[c] == RIPE:
            q.append((r, c))

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if Z > 1:
    drc.extend([(-R, 0), (R, 0)])

while q:
    r, c = q.popleft()

    for d in drc:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < rows and 0 <= nc < C and box[nr][nc] == UNRIPE:
            if (d[0] == 1 and nr % R == 0) or (d[0] == -1 and r % R == 0):
                continue

            q.append((nr, nc))
            box[nr][nc] = box[r][c] + 1

result = 0
for r in box:
    for c in r:
        if c == UNRIPE:
            print(-1)
            exit(0)
        result = max(result, c)

print(result - 1)


# 2차원 리스트

from collections import *
from sys import *

stdin = open("7569.txt", "r")

RIPE, UNRIPE = 1, 0

C, R, Z = map(int, stdin.readline().split())
rows = R * Z

box = [list(map(int, stdin.readline().split())) for _ in range(rows)]
q = deque()

for r, row in enumerate(box):
    for c in range(C):
        if row[c] == RIPE:
            q.append((r, c))

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if Z > 1:
    drc.extend([(-R, 0), (R, 0)])

while q:
    r, c = q.popleft()

    for d in drc:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < rows and 0 <= nc < C and box[nr][nc] == UNRIPE:
            if (d[0] == 1 and nr % R == 0) or (d[0] == -1 and r % R == 0):
                continue
            q.append((nr, nc))
            box[nr][nc] = box[r][c] + 1

result = 0
for r in box:
    for c in r:
        if c == UNRIPE:
            print(-1)
            exit(0)
        result = max(result, c)

print(result - 1)
