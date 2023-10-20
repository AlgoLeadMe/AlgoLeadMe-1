def find_the_biggest_prime_number(num):
    temp_list = []
    for x in range(2,int(num**0.5)+1):
            
        if num%x==0:
            temp_list.append(num/x)
            if num/x <= 10_000_000:
                return num/x
                
    else:
        temp_list.reverse()
        for temp_num in temp_list:
            if num//temp_num <= 10_000_000:
                return num//temp_num
        
        else:
            return 1 if num != 1 else 0
    
def solution(begin, end):
    answer = []
    
    for num in range(end,begin-1,-1):
        answer.append(find_the_biggest_prime_number(num))
    
    answer.reverse()
    return answer