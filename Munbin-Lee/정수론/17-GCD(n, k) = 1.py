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


def dfs(cur, curBit):
    global answer
    if cur == len(factors):
        if curBit == 0: return
        prod = 1
        for idx, factor in enumerate(factors):
            if curBit & (1 << idx):
                prod *= factor
        hasEvenBit = bin(curBit).count('1') % 2 == 0
        answer += n // prod * (hasEvenBit and 1 or -1)
        return

    dfs(cur + 1, curBit)
    dfs(cur + 1, curBit | (1 << cur))


dfs(0, 0)

print(answer)
