def solution(food):
    left = ''
    for i in range(1,len(food)):
        left += str(i)*(food[i]//2)
    right = ''.join(reversed(list(left)))
    return left+'0'+right