from collections import deque

total_case_count = int(input())

for _ in range(total_case_count):
    total_team_count = int(input())
    before_ranks = {idx+1 : rank for idx, rank in enumerate(map(int,input().split(" ")))}

    highers = [[] for _ in range(total_team_count+1)]
    indegrees = [0 for _ in range(total_team_count+1)]

    temp = []
    for rank in range(total_team_count,0,-1):
        team = before_ranks[rank]        

        highers[team] = temp[:]
        indegrees[team] = total_team_count - len(temp) - 1
        temp.append(team)

    change_count = int(input())

    for _ in range(change_count):
        changer1, changer2 = map(int, input().split(" "))
        
        if changer1 in highers[changer2]:
            indegrees[changer2] += 1
            indegrees[changer1] -= 1

            highers[changer2].remove(changer1)
            highers[changer1].append(changer2)

        elif changer2 in highers[changer1]:
            indegrees[changer1] += 1
            indegrees[changer2] -= 1

            highers[changer1].remove(changer2)
            highers[changer2].append(changer1)

    deq = deque([])

    for idx, indegree in enumerate(indegrees):
        if indegree == 0 and idx != 0:
            deq.append(idx)

    answer = []
    while deq:
        
        if len(deq) >= 2:
            print("?")
            break
            
        now = deq.popleft()
        answer.append(now)

        for higher in highers[now]:
            indegrees[higher] -= 1

            if indegrees[higher] == 0:
                deq.append(higher)

    else:
        
        if sum(indegrees) > 0:
            print("IMPOSSIBLE")
            continue

        else:
            print(*answer)