def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        alpha = alpha.replace(i,"")
       
    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]
    return answer