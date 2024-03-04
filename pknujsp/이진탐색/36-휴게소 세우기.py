N, M, L = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

left = 1
right = L - 1

min_max_distance = right

while left <= right:
    max_distance = (left + right) // 2
    extra_added = 0
    last_installed_x = 0
    
    for installed_x in array:
        if installed_x - last_installed_x > max_distance:
            extra_added += (installed_x - last_installed_x - 1) // max_distance
            
        last_installed_x = installed_x
        
    if L - last_installed_x > max_distance:
        extra_added += (L - last_installed_x - 1) // max_distance

    if extra_added > M:
        left = max_distance + 1
    else:
        right = max_distance - 1

print(left)
    