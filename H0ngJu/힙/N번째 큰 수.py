import sys
import heapq

line = int(sys.stdin.readline().strip())

heap = []
heapq.heapify(heap)

for i in range(line):
    data = list(map(int, sys.stdin.readline().strip().split()))
    for s in data:
        if len(heap) < line:
            heapq.heappush(heap, s)
        else:
            if s > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, s)

print(heap[0])