import heapq

total_problem_count, total_information_count = map(int,input().split(" "))

informations = [[] for _ in range(total_problem_count+1)]
indegrees = [0 for _ in range(total_problem_count+1)]

for _ in range(total_information_count):
    before, after = map(int, input().split(" "))
    informations[before].append(after)
    indegrees[after] += 1

_heap = []
for idx, indegree in enumerate(indegrees):
    if indegree == 0 and idx != 0:
        heapq.heappush(_heap,idx)

while _heap:
    now = heapq.heappop(_heap)
    print(now, end = " ")

    for information in informations[now]:
        indegrees[information] -= 1

        if indegrees[information] == 0:
            heapq.heappush(_heap,information)