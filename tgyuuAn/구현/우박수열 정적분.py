def collatz(number):
    count = 0
    y = []
    
    while number != 1:    
        y.append(number)
            
        if number%2==0:
            number/=2        
        
        else:
            number = number*3+1
        
        count += 1
        
    y.append(1)
    
    return count, y

def solution(k, ranges):
    answer = []
    n,y =collatz(k)
    area = [min(y[x],y[x-1]) + abs(y[x]-y[x-1])/2 for x in range(1,n+1)]
    
    for ran in ranges:
        start_x, end_x = ran[0], n+ran[1]
        
        
        if start_x==end_x:
            answer.append(0)
            continue
        
        if start_x > end_x:
            answer.append(-1)
            continue
        
        answer.append(sum(area[start_x:end_x]))
        
    return answer