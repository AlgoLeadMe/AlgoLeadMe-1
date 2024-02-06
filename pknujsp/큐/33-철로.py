from sys import *
from heapq import *

points = []

for _ in range(int(stdin.readline().strip())):
    h, o = map(int, stdin.readline().strip().split())
    points.append([min(h, o), max(h, o)])

points.sort(key=lambda x: x[1])
D = int(stdin.readline().strip())

max_users = 0
start_points_list = []

for start, destination in points:
    if start + D < destination:
        continue
    heappush(start_points_list, start)
    
    while start_points_list:
        if start_points_list[0] + D >= destination:
            break
        heappop(start_points_list)
        
    max_users = max(max_users, len(start_points_list))

print(max_users)
