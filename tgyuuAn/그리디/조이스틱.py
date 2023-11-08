    #65 ~ 77 -> 77이하면 A부터 위로,
    #78은 아무거나 상관없음.
    #91 ~ 79 -> 79이상이면 A부터 아래로
    
def make_char_try_number(target):
    target_ascii = ord(target)
    
    if target_ascii <= 78 and target_ascii >= 65:
        return target_ascii-65
    
    else: 
        return 91-target_ascii
    
def solution(name):
    answer = 0
    index = len(name)//2
    tot_count = 0

    max_A_count = -1
    max_A_idx = [0,0]
    
    start_char_idx = -1
    end_char_idx = -1
    
    temp = 0
    temp_idx = 0
    flag = False
    for idx,char in enumerate(name):
        if char == "A":
            if flag == False:
                flag = True
                temp_idx = idx

            temp += 1   
        
        else:
            
            if start_char_idx == -1:
                start_char_idx = idx
            
            end_char_idx = idx
            
            if flag == True:    
                flag = False
                
                if max_A_count < temp:
                    max_A_count = temp
                    max_A_idx = [temp_idx,temp_idx+temp]

            temp = 0

                    
    if flag == True:
        if max_A_count < temp:
            max_A_count = temp
            max_A_idx = [temp_idx,temp_idx+temp]
            
    #1. 앞에 먼저 갔다가, 다시 뒤로 돌아가는 경우
    #2. 뒤로 먼저 갔다가, 다시 앞으로 돌아가는 경우
    #3. 그냥 지나가는 경우.

    if max_A_count != -1:
        #A로만 이루어진 경우 ex)AAAAA
        if max_A_idx == [0,len(name)]:
            return 0
        
        #뒷 부분이 A로 끝나는 경우 ex)BBAAA
        elif max_A_idx[1] == len(name):
            answer += max_A_idx[0]-1
            
        #앞 부분이 A로 시작하는 경우 ex)AAABB
        elif max_A_idx[0] == 0:
            answer += len(name)-max_A_idx[1]
        
        #앞 부분, 뒷 부분 다 A로 시작하는 경우 ex )AABBBA
        elif name[0] == "A" and name[-1] == "A":
            
            #앞으로 지나가는 것
            if end_char_idx < len(name)-start_char_idx and end_char_idx < (max_A_idx[0]-1)*2 + len(name)-max_A_idx[1] and end_char_idx < (len(name)-max_A_idx[1])*2 + max_A_idx[0]-1:
                answer += end_char_idx
            
            #뒤로 지나가는 것
            elif len(name)-start_char_idx <= end_char_idx and len(name)-start_char_idx < (max_A_idx[0]-1)*2 + len(name)-max_A_idx[1] and len(name)-start_char_idx < (len(name)-max_A_idx[1])*2 + max_A_idx[0]-1:
                answer += len(name)-start_char_idx
                
            #A의 시작 지점 까지 가는 것이 더 짧을 경우
            elif max_A_idx[0]-1 < len(name)-max_A_idx[1]: 
                answer += (max_A_idx[0]-1)*2 + len(name)-max_A_idx[1]
            
            #A의 끝 지점으로 갓다 가는게 더 짧을 경우
            elif len(name)-max_A_idx[1] < max_A_idx[0]-1:
                answer += (len(name)-max_A_idx[1])*2 + max_A_idx[0]-1
            
        #그 외 ex)BBAAABBB
        else:
            #그냥 지나가는 것이 더 짧을 경우
            if len(name)-1 <= ((len(name)-max_A_idx[1])*2 + max_A_idx[0]-1) and len(name)-1 <= ((max_A_idx[0]-1)*2 + len(name)-max_A_idx[1]) :
                answer += len(name)-1
                    
            #A의 시작 지점 까지 가는 것이 더 짧을 경우
            elif max_A_idx[0]-1 < len(name)-max_A_idx[1]: 
                answer += (max_A_idx[0]-1)*2 + len(name)-max_A_idx[1]
            
            #A의 끝 지점으로 갓다 가는게 더 짧을 경우
            elif len(name)-max_A_idx[1] < max_A_idx[0]-1:
                answer += (len(name)-max_A_idx[1])*2 + max_A_idx[0]-1
                
    #A가 없는 경우 ex)JEROEN
    else:
        answer += len(name)-1
    
    
    for char in name:
        if char == "A":
            continue
            
        else:
            answer += make_char_try_number(char)
    
    return answer