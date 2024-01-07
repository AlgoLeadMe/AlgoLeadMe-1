sequence_length = int(input())

sequence = list(map(int,input().split()))

swap_count = int(input())
idx = 0
while True:
    if idx == sequence_length:
        break

    # 교환 가능환 횟수 안에서 도달할 수 있는 가장 큰 수를 찾음
    _max = -1
    max_idx = idx
    for elem_idx, element in enumerate(sequence[idx:min(sequence_length,idx+swap_count+1)]):
        if(element > _max):
            _max = element
            max_idx = elem_idx + idx

    # 바꾸지 않은 상태가 크거나 같을 경우 바꾸지 않음
    if max_idx == idx:
        idx += 1
        continue
    
    for swap_idx in range(max_idx,idx,-1):
        sequence[swap_idx],sequence[swap_idx-1] = sequence[swap_idx-1], sequence[swap_idx]
    
    swap_count -= (max_idx - idx)
    idx += 1

    # print(idx, swap_count)

print(*sequence)