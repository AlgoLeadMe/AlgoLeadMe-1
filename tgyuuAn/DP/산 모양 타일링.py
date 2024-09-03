def solution(n, tops):
    top = set()
    DIV = 10_007
    
    count = 0
    for idx, element in enumerate(tops):
        if element==1: 
            count += 1
            top.add(2*(idx+1)+count)

    DP = [0 for _ in range((n*2)+1+count+1)]
    DP[1] = 1
    DP[2] = 2
    
    for now_idx in range(3,len(DP)):
        if (now_idx-1) in top: DP[now_idx] = (DP[now_idx-3] % DIV) + (DP[now_idx-1] % DIV) % DIV
        else: DP[now_idx] = (DP[now_idx-2] % DIV) + (DP[now_idx-1] % DIV) % DIV
    
    return DP[-1] % DIV