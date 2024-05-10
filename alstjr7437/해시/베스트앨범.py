def solution(genres, plays):
    answer = []
    dict = {}

    # 딕셔너리 만들기
    for i in range(len(genres)):
        if genres[i] not in dict :
            dict[genres[i]] = [[plays[i], i]]
        else :
            dict[genres[i]].append([plays[i],i])
            
    # 딕셔너리 안에 재생회수로 재정렬
    for genres, plays in dict.items():
        dict[genres] = sorted(plays, key=lambda x: x[0], reverse=True)

    # 각 장르 총합 계산
    totals = {i: sum(j[0] for j in songs) for i, songs in dict.items()}

    # 총합 기준으로 딕셔너리 순서 변경
    sorted_data = {k: v for k, v in sorted(dict.items(), key=lambda item: totals[item[0]], reverse=True)}


    # 정답 인덱스 추가 부분
    for i in sorted_data.values():
        answer.append(i[0][1])
        if len(i) != 1:
            answer.append(i[1][1])
        
    
    return answer