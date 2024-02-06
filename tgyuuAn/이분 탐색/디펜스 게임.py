def solution(n, k, enemy):
    
    left = 0
    right = len(enemy)
    
    while True:
        mid = (left + right)//2

        if left>right:
            break
            
        now_enemy = sorted(enemy[:mid])

        for _ in range(k):
            if now_enemy:
                now_enemy.pop()
                
            else:
                break

        temp = sum(now_enemy)
        
        if temp > n :
            right = mid-1
            
        elif temp < n :
            left = mid+1
            
        else:
            return mid
    
    return mid