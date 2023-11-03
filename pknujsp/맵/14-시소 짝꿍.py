def solution(weights):
    weight_dict = {}
    for w in weights:
        # weight의 개수 확인
        weight_dict[w] = weight_dict.get(w, 0) + 1

    total_count = 0
    divisors = (2, 3, 4)
    b_weight = 0

    for a_weight, num in weight_dict.items():
        if num >= 2:
            # 조합의 개수 numC2 계산
            total_count += num * (num - 1) // 2

        for divisor in divisors:
            # B의 몸무게가 A몸무게의 50%, 66.6%, 75%일때 중심으로 부터 2~4미터의 거리에 앉아서 균형을 맞출수 있다
            b_weight = a_weight - a_weight / divisor
            if b_weight in weight_dict:
                total_count += weight_dict[b_weight] * num

    return total_count
