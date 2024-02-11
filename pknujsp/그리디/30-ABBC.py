from collections import *
from sys import *

stdin = open('25381.txt')
string = list(stdin.readline().strip())

aq = deque()
bq = deque()
cq = deque()

for i, char in enumerate(string):
    if char == 'A':
        aq.append(i)
    elif char == 'B':
        bq.append(i)
    else:
        cq.append(i)

count = 0

while bq and cq:
    b = bq[0]
    while cq:
        c = cq.popleft()
        if b < c:
            bq.popleft()
            count += 1
            break

while aq and bq:
    a = aq.popleft()
    while bq:
        b = bq.popleft()
        if a < b:
            count += 1
            break

print(count)