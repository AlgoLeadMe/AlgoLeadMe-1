from collections import deque

def solution(picks, minerals):
    total_len = len(minerals)
    total_can_pick = sum(picks) * 5
    
    stone_board= {"diamond" : 25, "iron" : 5, "stone" : 1}
    iron_board = {"diamond" : 5, "iron" : 1, "stone" : 1}
    diamond_board = {"diamond" : 1, "iron" : 1, "stone" : 1}

    stone_sum_list = []
    iron_sum_list = []
    diamond_sum_list = []
    temp_list = []
    
    total_len = min(total_len, total_can_pick)
    
    for x in range(0,total_len,5):
        
        stone_sum, iron_sum, diamond_sum = 0, 0, 0
        
        for mineral in minerals[x:x+5]:
            stone_sum += stone_board[mineral]
            iron_sum += iron_board[mineral]
            diamond_sum += diamond_board[mineral]
        
        temp_list.append([stone_sum,x//5])
        stone_sum_list.append(stone_sum)
        iron_sum_list.append(iron_sum)
        diamond_sum_list.append(diamond_sum)
        
    temp_list.sort(key = lambda x : x[0] , reverse=True)
    temp_list = deque(temp_list)
    
    answer = 0

    while temp_list:
        now = temp_list.popleft()
        now_index = now[1]
        
        if picks[0] > 0:
            answer += diamond_sum_list[now_index]
            picks[0] -= 1
        
        elif picks[1] > 0:
            answer += iron_sum_list[now_index]
            picks[1] -= 1

        elif picks[2] > 0:
            answer += stone_sum_list[now_index]
            picks[2] -= 1
    
    return answer