from collections import defaultdict
from heapq import *

socket_count, use_count = map(int,input().split())
use_list = list(map(int,input().split()))

now_socket = []
answer = 0
for idx, use in enumerate(use_list):
    # print(now_socket, use)
    if use in now_socket:
        continue
    
    if len(now_socket) < socket_count:
        now_socket.append(use)
        continue

    else:
        candidate = []
        for check_idx, using in enumerate(now_socket):
            try:
                next_idx = use_list[idx:].index(using)
            
            # 찾지 못했을 경우 코스트를 최대로 올림
            except:
                next_idx = 101

            heappush(candidate,[-next_idx,check_idx])

        next_idx, remove_idx = heappop(candidate)

        now_socket[remove_idx] = use
        answer += 1

print(answer)