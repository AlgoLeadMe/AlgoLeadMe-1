from heapq import *

def solution(food_times, k):
    foods = [(food_times[i], i) for i in range(len(food_times))]
    heapify(foods)
    
    remaining_time = k
    # 진행할 때마다 이전 식사 시간이 중복되어 연산되므로 빼야함
    prev_meal_time = 0
    
    while foods:
        time = foods[0][0]
        meal_time = (time - prev_meal_time) * len(foods)
        if meal_time > remaining_time:
            break
            
        heappop(foods)
        remaining_time -= meal_time
        prev_meal_time = time

    if not foods:
        return -1
    
    foods.sort(key=lambda x: x[1])
    
    restart_food_idx = remaining_time % len(foods)
    restart_food = foods[restart_food_idx][1] + 1
    
    return restart_food
    