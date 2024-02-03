def solution(storey):
    answer = []
   
    def dfs(st, count):
        if st == 0:
            answer.append(count)
            return
       
        one = st % 10
        up = 10-one
        down = one
       
        if up < down: #올라가는 게 최소일 때
            dfs(st // 10 + 1, count + up) #층수가 높아지므로 +1
           
        elif down < up: #내려가는 게 최소일 때
            dfs(st //10, count + down)
           
        else: #올라가는 횟수, 내려가는 횟수 같을 때는 둘 다 시도
            for i in range(2):
                dfs(st // 10 + i, count + up)
   
    dfs(storey, 0)
   
    return min(answer)