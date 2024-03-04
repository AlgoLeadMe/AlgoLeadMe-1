total_app_count, need_memory = map(int,input().split())

use_memory = list(map(int,input().split()))
re_use_cost = list(map(int,input().split()))

dp_table = [0 for _ in range(sum(re_use_cost)+1)]
cost_sum = sum(re_use_cost)

for memory, cost in zip(use_memory, re_use_cost):
    for idx in range(cost_sum,cost-1,-1):
        dp_table[idx] = max(dp_table[idx], dp_table[idx-cost] + memory)

for idx, memory in enumerate(dp_table):
    if memory >= need_memory: 
        print(idx)
        break