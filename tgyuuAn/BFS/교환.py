from collections import Counter

number, exchange_count = map(int,input().split())

number = list(str(number))
answer = "0"

counter = Counter(number)
same_number_flag = False

for key, value in counter.items():
    if value >=2:
        same_number_flag = True 
        break

def dfs(number, depth, remain_exchange_count, same_number_flag):
    global answer

    if remain_exchange_count == 0:
        answer = max(answer, "".join(number))
        return

    flag = False
    for prev_idx in range(depth,len(number)):
        for next_idx in range(prev_idx+1, len(number)):
            if number[next_idx] >= number[prev_idx]:
                number[next_idx], number[prev_idx] = number[prev_idx], number[next_idx]
                dfs(number, depth+1, remain_exchange_count-1, same_number_flag)
                number[next_idx], number[prev_idx] = number[prev_idx], number[next_idx]
                flag = True

    if flag == False:
        if same_number_flag: dfs(number, depth+1, remain_exchange_count-1, same_number_flag)
        else:
            number[-1], number[-2] = number[-2], number[-1]
            dfs(number, depth+1, remain_exchange_count-1, same_number_flag)
            number[-1], number[-2] = number[-2], number[-1]

if len(number) == 1 and exchange_count >= 1:
    print("-1")

elif len(number) == 2 and "0" in number:
    print("-1")

else:
    dfs(number,0, exchange_count, same_number_flag)
    print(answer)