def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pickup = 0
    for i in range(n-1, -1, -1):
        print(f"{deliver} + {deliveries[i]} = {deliver + deliveries[i]}")
        print(f"{pickup} + {pickups[i]} = {pickup + pickups[i]}")
        deliver += deliveries[i]
        pickup += pickups[i]

        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += (i+1) * 2
            print(deliver, pickup)
            print(f"차 거리{(i+1)}")
        
    return answer


solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0])
