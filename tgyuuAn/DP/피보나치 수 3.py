target = int(input())

M = 1_000_000
period = 1_500_000

target %= period

dp_table = [0 for _ in range(3)]
dp_table[0] = 0
dp_table[1] = 1

for idx in range(2,target+1):
    idx %= 3
    dp_table[idx] = dp_table[idx-1] % M + dp_table[idx-2] % M

print(dp_table[target%3]%M)