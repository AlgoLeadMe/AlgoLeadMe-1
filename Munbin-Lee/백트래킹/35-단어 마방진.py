from itertools import permutations

stdin = open(0)

L, N = map(int, stdin.readline().split())
words = sorted(stdin.read().splitlines())

# 단어 순열 x가 단어 마방진인지 확인하는 함수
def isValid(x):
    for i in range(L):
        for j in range(L):
            if x[i][j] != x[j][i]: return False
    
    return True

for perm in permutations(words, L):
    if not isValid(perm): continue
    
    print(*perm, sep='\n')
    exit()

print('NONE')