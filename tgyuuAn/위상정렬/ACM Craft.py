from collections import deque, defaultdict

test_case = int(input())

for _ in range(test_case):

    building_count, constructor_flow_length = map(int,input().split(" "))
    building_count = int(building_count)
    
    building_time = [0]
    building_time.extend(list(map(int,input().split(" "))))

    constructor_flow = []
    for _ in range(constructor_flow_length):
        before, after = map(int,input().split(" "))
        constructor_flow.append([before, after])

    target_number = int(input())

    indegree_dic = defaultdict(int)
    child_dic = defaultdict(list)

    for flow in constructor_flow:
        before, after = flow
        indegree_dic[after] += 1
        child_dic[before].append(after)
    
    deq = deque([])
    dp_table = [int(-1) for _ in range(building_count+1)]
    for n in range(1,building_count+1):
            if indegree_dic[n] == 0:
                 deq.append(n)
                 dp_table[n] = building_time[n]

    while deq:
        now = deq.popleft()
        childs = child_dic[now]
        
        for child in childs:
             indegree_dic[child] -= 1
             dp_table[child] = max(dp_table[child], dp_table[now]+building_time[child])

             if indegree_dic[child] == 0:
                  deq.append(child)
                  
    print(dp_table[target_number])