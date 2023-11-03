from heapq import *

def solution(book_times):
    # 시각을 정수로 파싱
    for book_time in book_times:
        for k, v in enumerate(book_time):
            h, m = map(int, v.split(':'))
            book_time[k] = h * 60 + m;
    
    # 방의 사용 가능 시각을 힙에 저장
    rooms = [0]
    
    for book_time in sorted(book_times):
        start, end = book_time
        
        # 객실 사용
        if rooms[0] <= start:
            heappop(rooms)
            heappush(rooms, end + 10)
        
        # 사용 가능한 객실이 없을 경우 객실 추가
        else:
            heappush(rooms, end + 10)
        
    return len(rooms)