def solution(n, info):
    answer = []  
    ryan = [0]*11
    diff = 0 

    def dfs(m, idx):
        nonlocal answer, diff, ryan 

        if m == n:
            r_score, a_score = 0, 0

            # 라이언과 어피치의 점수 계산
            for j in range(11):
                if ryan[j] > info[j]:
                    r_score += 10 - j
                elif 0 != info[j] and ryan[j] <= info[j]:
                    a_score += 10 - j

            # 라이언이 얻은 점수가 더 높을 때
            if r_score > a_score:
                # 격차가 더 크다면 현재의 화살 배치를 답으로 설정
                if diff < r_score - a_score:
                    diff = r_score - a_score
                    answer = ryan[:]

                # 격차가 같다면 낮은 점수를 더 많이 쏜 걸로 갱신
                elif diff == r_score - a_score:
                    for i in range(10, -1, -1):
                        if ryan[i] < answer[i]:
                            break
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
            return

        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m+1, i)
            ryan[i] -= 1

    dfs(0, 0)

    return answer if answer else [-1]
