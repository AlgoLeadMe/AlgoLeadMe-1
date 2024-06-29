import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
data = list(map(int, input().split()))
diff = [0] * N

for i in range(N-1):
    diff[i] = data[i+1] - data[i]

diff.sort(reverse=True)

total_diff = sum(diff)

for i in range(K-1):
        total_diff -= diff[i]

print(total_diff)