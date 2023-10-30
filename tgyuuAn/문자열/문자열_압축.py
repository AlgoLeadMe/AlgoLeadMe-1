def solution(s):
    len_total_s = len(s)
    answer = int(1e9)
    
    if len_total_s == 1:
        return 1
    
    for len_s in range(1,len_total_s):
        stack = []     
        temp_list_for_string = []
        
        for char_idx in range(0,len_total_s,len_s):
            now = s[char_idx:char_idx+len_s]

            if len(stack) > 0 and now == stack[-1]:
                temp_list_for_string[-1][1] += 1
                continue
                
            temp_list_for_string.append([now,1])
            stack.append(now)

        temp_str = ""
        for key, value in temp_list_for_string:
            if value != 1:
                temp_str += str(value)

            temp_str += key
        answer = min(answer,len(temp_str))
        
    return answer