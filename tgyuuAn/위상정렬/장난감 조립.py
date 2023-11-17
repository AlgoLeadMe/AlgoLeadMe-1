from collections import deque, defaultdict

total_toy_type = int(input())
length_toy_combination_recipe = int(input())
indegree = list(0 for _ in range(total_toy_type+1))
toy_combination_recipe = defaultdict(dict)

for _ in range(length_toy_combination_recipe):
    target_toy, part_toy, count = map(int,input().split(" "))
    toy_combination_recipe[part_toy][target_toy] = count
    indegree[target_toy] += 1

dp_table = defaultdict(dict)
deq = deque([])
for idx in range(1,total_toy_type+1):
    if indegree[idx] == 0:
        deq.append(idx)
        dp_table[idx][idx] = 1

while deq:
    now = deq.popleft()
    now_toy_part = dp_table[now]
    can_toy_combination = toy_combination_recipe[now]

    for target_toy, count in can_toy_combination.items():
        indegree[target_toy] -= 1
        
        for toy_part, need_count in now_toy_part.items():
            
            if toy_part not in dp_table[target_toy].keys():
                dp_table[target_toy][toy_part] = need_count * count
                continue

            dp_table[target_toy][toy_part] += need_count * count

        if indegree[target_toy] == 0:
            deq.append(target_toy)

for part_toy, count in sorted(dp_table[total_toy_type].items()):
    print(part_toy, count)