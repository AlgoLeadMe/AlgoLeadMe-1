from heapq import *
import sys

total_numbers_count = int(sys.stdin.readline())

min_heap = []
max_heap = []
numbers = []

for _ in range(total_numbers_count):
    number = int(sys.stdin.readline())
    if len(min_heap) == len(max_heap): heappush(max_heap,-1*number)
    else: heappush(min_heap,number)

    if min_heap and min_heap[0] < -1*max_heap[0]:
        a = heappop(min_heap)
        b = heappop(max_heap)

        heappush(max_heap,-1*a)
        heappush(min_heap,-1*b)

    print(-1*max_heap[0])