from heapq import *
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    q = int(input())

    # 최소힙만 지원해서 최대, 최소 만들어주기
    min_heap = []
    max_heap = []
    nums = [False] * q  # 동기화를 위한 부분

    for i in range(q):
        k = list(input().split())
        iNum = int(k[1])  

        # 입력 부분
        if k[0] == "I" :
            heappush(min_heap, (iNum,i))    # 동기화를 위한 i도 튜플로 넣어주기
            heappush(max_heap, (-iNum, i))
            nums[i] = True
        elif iNum == 1:
            while max_heap and not nums[max_heap[0][1]]:   
                heappop(max_heap)
            if max_heap:     # max_heap에서 작은 수 제거
                nums[max_heap[0][1]] = False 
                heappop(max_heap)
        else:
            while min_heap and not nums[min_heap[0][1]]:    # 이미 삭제된 노드인 경우 삭제되지 않은 노드 나올때까지 모두 버림
                heappop(min_heap)
            if min_heap:    # min_heap에서 작은 수(삭제 노드) 제거
                nums[min_heap[0][1]] = False
                heappop(min_heap)
        # print(min_heap, max_heap, nums, k)
    # 모든 연산 후 동기화 되지 않은 노드 처리
    while min_heap and not nums[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not nums[max_heap[0][1]]:
        heappop(max_heap)

    if max_heap and min_heap :
        print(-max_heap[0][0], min_heap[0][0])
    else :
        print("EMPTY")