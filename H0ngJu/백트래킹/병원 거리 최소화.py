import sys

def input() : return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
hospital = []
person = []
info = [[] for _ in range(n)]

# 사람, 병원 정보 받기
for i in range(n):
    info[i].extend(list(map(int, input().split())))
    for j in range(n):
        if info[i][j] == 2:
            hospital.append((i,j))
        if info[i][j] == 1:
            person.append((i,j))

distance = [[0 for _ in range(len(hospital))] for _ in range(len(person))]

for i in range(len(person)):
    px, py = person[i]
    for j in range(len(hospital)):
        hx, hy = hospital[j]
        distance[i][j] = abs(px-hx) + abs(py-hy)

# hospital 위치 중에 m개를 선택해서 최솟값 구하기
hospital_arr = [i for i in range(len(hospital))]
all_combinations = []

def combination(start, depth, combination_arr):
    if depth == m: # m만큼 찾으면 return
        all_combinations.append(combination_arr[:])
        return
    for i in range(start, len(hospital_arr)):
        combination_arr.append(hospital_arr[i]) # 원소 일단 넣고
        combination(i + 1, depth + 1, combination_arr) # 재귀 돌림
        combination_arr.pop() # 다시 뽑은거 복귀 -> [1,2,3]을 구하면, 3빼고 다시 다음 반복문 넣어서 [1,2,4] 가능

combination(0, 0, [])

min_distance_sum = 1e9
for hospitals_combination in all_combinations:
    cur_distance = 0
    
    for i in range(len(person)):
        dist = 1e9
        for j in hospitals_combination:
            dist = min(dist, distance[i][j])
        cur_distance += dist

    min_distance_sum = min(min_distance_sum, cur_distance)

print(min_distance_sum)

# --- combination -----

# import sys
# import itertools

# def input() : return sys.stdin.readline().rstrip()

# n, m = map(int, input().split())
# hospital = []
# person = []
# info = [[] for _ in range(n)]

# # 사람, 병원 정보 받기
# for i in range(n):
#     info[i].extend(list(map(int, input().split())))
#     for j in range(n):
#         if info[i][j] == 2:
#             hospital.append((i,j))
#         if info[i][j] == 1:
#             person.append((i,j))

# distance = [[0 for _ in range(len(hospital))] for _ in range(len(person))]

# for i in range(len(person)):
#     px, py = person[i]
#     for j in range(len(hospital)):
#         hx, hy = hospital[j]
#         distance[i][j] = abs(px-hx) + abs(py-hy)

# # hospital 위치 중에 m개를 선택해서 최솟값 구하기

# min_distance_sum = 1e9
# combbination_arr = [i for i in range(len(hospital))]

# for hospitals_combination in itertools.combinations(combbination_arr, m):
#     cur_distance = 0
    
#     for i in range(len(person)):
#         dist = 1e9
#         for j in hospitals_combination:
#             dist = min(dist, distance[i][j])
#         cur_distance += dist

#     min_distance_sum = min(min_distance_sum, cur_distance)

# print(min_distance_sum)

# # 빈자리면 0, 사람이면 1, 병원이면 2
# # 출력은 최소 거리

# # 병원의 수 만큼 배열을 생성해서, 각 사람마다의 최소 거리를 계산한다.
# # 각 병원의 거리 총 합을 계산해서 정렬한다. -> 문제 : 사람마다 다른 병원이 최소 거리일 수 있지만, 해당 가능성을 무시하게 됨

# # 각 사람마다 각 병원의 거리를 계산한다.
# # [[1,2,4,5], [1,2,4,5]]의 형태
# # 병원 중 m개를 고르는 조합
# # 조합에서 최소거리 갱신하여 찾기