def solution(N, stages):
    stage_player_counts = [0] * (N + 2)

    for stage in stages:
        stage_player_counts[stage] += 1

    failure_rates = []
    players_reached = len(stages)

    for stage in range(1, N + 1):
        if stage_player_counts[stage] == 0:
            failure_rates.append((stage, 0.0))
            continue

        failure_rate = stage_player_counts[stage] / players_reached
        failure_rates.append((stage, failure_rate))

        players_reached -= stage_player_counts[stage]

    # 실패율 정렬, stage 번호 목록 생성
    failure_rates.sort(key=lambda x: x[1], reverse=True)
    failure_rates = list(map(lambda x: x[0], failure_rates))

    return failure_rates
