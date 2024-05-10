def solution(clothes):
    dict = {}
    for value,key in clothes:
        if key not in dict:
            dict[key] = 1
        dict[key] += 1
    
    answer = 1
    
    for key,value in dict.items():
        answer *= value
        
    return answer - 1