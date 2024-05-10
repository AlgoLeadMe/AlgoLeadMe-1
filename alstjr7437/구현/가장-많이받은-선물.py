"""
2024 카카오 겨울 인턴쉽 문제
https://school.programmers.co.kr/learn/courses/30/lessons/258712
"""
def solution(friends, gifts):
	# 친구들 인덱스 저장해두는 딕셔너리
    dict = {}
    for i in range(len(friends)):
        dict[friends[i]] = i

	# 선물 기록을 위한 전체 테이블1
    present = [[0] * len(friends) for _ in range(len(friends))]
    for i in gifts:
        key, val = i.split(" ")
        # 각 key val 잘라서 인덱스 딕셔너리를 활용해 테이블 만들기
        present[dict[key]][dict[val]] += 1
		
	# 선물 지수 저장을 위한 테이블2
    table = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            # i, j를 활용해 테이블1 데이터를 이용한 선물지수 만들기
            table[i] += present[i][j]
            table[j] -= present[i][j]

	# 결과 출력을 위한 result
    result = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            # 선물을 i가 선물을 더욱 많이 줬으면 선물 받기
            if present[i][j] > present[j][i]:
                result[i] += 1
            # j가 선물을 더욱 많이 줬으면 j가 선물 받기
            elif present[j][i] > present[i][j]:
                result[j] += 1
            # 선물을 똑같이 주고 받았으면
            else:
                # 선물 지수를 비교해서 i 또는 j에게 주기
                if table[i] > table[j]:
                    result[i] += 1
                if table[j] > table[i]:
                    result[j] += 1

		# 친구 중 선물을 제일 많이 받을 갯수 출력하기!
    return max(result)