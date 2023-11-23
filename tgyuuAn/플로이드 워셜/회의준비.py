from collections import deque

attending_person_count = int(input())
flow_count = int(input())

table = [[int(1e9) for _ in range(attending_person_count+1)] for _ in range(attending_person_count+1)]

for idx in range(0,attending_person_count+1):
    if idx == 0:
        continue

    table[idx][idx] = 0




for _ in range(flow_count):
    node1, node2 = map(int,input().split(" "))
    table[node1][node2] = table[node1][node2] + 1 if table[node1][node2] != int(1e9) else 1
    table[node2][node1] = table[node2][node1] + 1 if table[node2][node1] != int(1e9) else 1

for idx in range(1,attending_person_count+1):
    for before in range(1,attending_person_count+1):
        if before == idx:
            continue

        for after in range(1,attending_person_count+1):
            if after == before or after == idx:
                continue
            
            table[before][after] = min(table[before][after],table[before][idx] + table[idx][after])



total_family = []
visited = [False] * (attending_person_count + 1)

for start_idx in range(1,attending_person_count+1):
    if visited[start_idx] == True:
        continue

    deq = deque([])
    family = {start_idx}
    visited[start_idx] = True

    for idx, distance_connect_person in enumerate(table[start_idx]):

        if start_idx == idx or idx == 0:
            continue

        if visited[idx] == True:
            continue

        if distance_connect_person != int(1e9):
            deq.append(idx)
            family.add(idx)
            visited[idx] = True

    while deq:
        now = deq.popleft()

        for now_idx, distance in enumerate(table[now]):

            if now_idx == 0:
                continue

            if distance != int(1e9) and visited[now_idx] == False:
                deq.append(now_idx)
                family.add(now_idx)
                visited[now_idx] = True
                
    total_family.append(family)



representatives = []
for family in total_family:

    _min = int(1e9)
    representative_idx = -1

    for representative_candidate in family:
        
        score = max(filter(lambda x : x!=int(1e9),table[representative_candidate][1:]))

        if score < _min:
            _min = score
            representative_idx = representative_candidate

    representatives.append(representative_idx)



print(len(representatives))

for representative in sorted(representatives):
    print(representative)