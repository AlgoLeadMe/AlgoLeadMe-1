def convert_time_to_minute(time):
    hour,minute = time.split(":")
    return int(hour)*60+int(minute)

def solution(plans):
    
    total_len = len(plans)
    answer = []
        
    plans.sort(key = lambda x: x[1])
    
    for idx,plan in enumerate(plans):
        
        todo = plan[0]
        start_time = convert_time_to_minute(plan[1])
        left_time = int(plan[2])
        next_idx = min(idx+1, total_len-1)
        
        plans[idx] = ([todo, start_time,left_time, next_idx])

    stack = [plans[0]]
    visitied = [False] * total_len
    visitied[0] = True
    
    while stack:
        now = stack[-1]
        now_start_time, now_left_time = now[1], now[2]
        next_idx = now[3]
        
        if visitied[next_idx] == False:
            next_start_time = plans[next_idx][1]
            
            if now_start_time + now_left_time < next_start_time:
                answer.append(stack.pop()[0])
                
                if stack:
                    stack[-1][1] = now_start_time + now_left_time
                    stack[-1][3] = next_idx
                    continue
                    
            if now_start_time + now_left_time == next_start_time:
                answer.append(stack.pop()[0])
                visitied[next_idx] = True
                stack.append(plans[next_idx])
                continue
            
            if stack:
                stack[-1][2] -= (next_start_time - now_start_time)
            visitied[next_idx] = True
            stack.append(plans[next_idx])
        
        else:
            if stack:
                stack[-1][1] = now_start_time + now_left_time
            answer.append(stack.pop()[0])
        
    return answer