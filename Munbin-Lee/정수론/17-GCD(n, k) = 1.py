from itertools import combinations
from math import prod

tempN = n = int(open(0).read())
div = 2
factors = []

while div * div <= tempN:
    if tempN % div == 0:
        factors.append(div)
        tempN //= div
        while tempN % div == 0:
            tempN //= div
    div += 1

if tempN > 1:
    factors.append(tempN)

answer = n

for i in range(1, len(factors) + 1):
    for comb in combinations(factors, i):
        answer -= n // prod(comb) * (i % 2 and 1 or -1)

print(answer)
