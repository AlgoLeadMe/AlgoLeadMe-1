def solution(k, tangerine):
    answer = 0
    
    count_d = {}
    for i in tangerine:
        if i in count_d:
            count_d[i] += 1
        else:
            count_d[i] = 1
    
    sort_d = sorted(count_d.items(), key = lambda x: x[1], reverse = True)

    for i in sort_d:
        k -= i[1] #각 크기별 귤의 개수만큼 k에서 빼기
        answer += 1
        if k <= 0:
            break
                
    return answer