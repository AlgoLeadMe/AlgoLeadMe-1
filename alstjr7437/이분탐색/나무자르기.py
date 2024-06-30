n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in tree:
        if i > mid:
            temp += i - mid
    
    if temp >= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)

# result = min(tree)
# while True:
#     temp = 0
#     for i in tree:
#         if i > result :
#             temp += i - result
#     if temp <= m :
#         break
#     result += 1

# print(result)
