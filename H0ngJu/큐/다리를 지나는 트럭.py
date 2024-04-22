from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    onBridge = deque() # 현재 다리 위에 있는 트럭
    truckNum = 0 # 현재 다리 위에 있는 트럭 수
    sum = 0 # 현재 다리 위에 있는 트럭 무게의 합
    truck_weights = deque(truck_weights)

    while truck_weights or onBridge:
        time += 1
        
        # 트럭이 다리를 지나가는 경우 처리
        if onBridge and time - onBridge[0][1] >= bridge_length:
            sum -= onBridge.popleft()[0]
            truckNum -= 1
        
        # 다음 트럭이 다리에 올라갈 수 있는 경우 처리
        # 트럭이 있고 합이 weight을 넘지 않으며, 수가 bridge_length를 넘기지 않는 경우
        if len(truck_weights) != 0 and sum + truck_weights[0] <= weight and truckNum + 1 <= bridge_length:
            truck = truck_weights.popleft() # pop
            onBridge.append((truck, time)) # 다리 위의 truck에 tuple 추가
            sum += truck # 무게 추가
            truckNum += 1 # 건너고 있는 트럭 추가
    
    return time