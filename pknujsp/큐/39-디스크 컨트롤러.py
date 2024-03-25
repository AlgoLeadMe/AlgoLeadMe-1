from heapq import *
from collections import *

def solution(jobs):
    jobs = deque(sorted(jobs))
    jobs_num = len(jobs) 
    
    curr_time = wait_time = 0
    heap = []
    
    while heap or jobs:
        while jobs and jobs[0][0] <= curr_time:
            requested_time, duration = jobs.popleft()
            heappush(heap, (duration, requested_time))
            
        if heap:
            duration, requested_time = heappop(heap)
            
            curr_time += duration
            wait_time += curr_time - requested_time
        else:
            curr_time += 1
    
    return wait_time // jobs_num