def solution(name, yearning, photo):
 answer = []
 for person in photo:
    score= 0
    for n in person:
        if n in name:
           score += yearning[name.index[n]]
    answer.append(score)
 return answer