import sys

def input(): return sys.stdin.readline().rstrip()

N, C = map(int, input().split())
M = int(input())

delieveries = []
for _ in range(M):
    start, destination, size = map(int, input().split())
    delieveries.append((start, destination, size))
    
delieveries.sort(key = lambda x : (x[1], x[0]))
table = [C for _ in range(N+1)]

answer = 0
previous_start = 0
for delievery in delieveries:
    start, destination, capacity = delievery

    can_delievery = capacity
    for town in range(start, destination):
        can_delievery = min(can_delievery, table[town])
    
    for town in range(start, destination):
        table[town] -= can_delievery

    answer += can_delievery
    
print(answer)