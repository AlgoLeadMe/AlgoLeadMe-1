import sys

def input(): return sys.stdin.readline().rstrip()

A, B = map(int, input().split())

bits = [0 for _ in range(len(bin(B)[2:]))]

for step in range(len(bits)):
    one_count_per_bundle = (2**step)
    total_count_bundle = 2 * (one_count_per_bundle)
    
    B_d, B_m = divmod(B,total_count_bundle)
    B_count = one_count_per_bundle * B_d
    if(B_m >= one_count_per_bundle): B_count += min(one_count_per_bundle,(B_m - one_count_per_bundle + 1))
    
    A_d, A_m = divmod(A-1,total_count_bundle)
    A_count = one_count_per_bundle * A_d
    if(A_m >= one_count_per_bundle): A_count += min(one_count_per_bundle, (A_m - one_count_per_bundle + 1))
    bits[step] += (B_count - A_count)
    
print(sum(bits))