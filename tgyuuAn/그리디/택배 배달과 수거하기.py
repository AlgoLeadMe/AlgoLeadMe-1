def solution(cap, n, deliveries, pickups):

    answer = 0
    cap_deliveries = 0
    cap_pickups = 0
    
    for idx in range(n-1,-1,-1):

        cap_deliveries += deliveries[idx]
        cap_pickups += pickups[idx]
        count = 0

        while cap_deliveries > 0 or cap_pickups > 0:
            
            cap_deliveries -= cap
            cap_pickups -= cap
            count += 1
            
        answer += (idx+1)*2*count
        
    return answer