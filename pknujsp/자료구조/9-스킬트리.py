def solution(skill, skill_trees):
    count = 0
    skill_sequence = {s: i for (i, s) in enumerate(skill)}
    
    for skill_tree in skill_trees:
        previous_skill_position = -1
        is_available = True
        
        for s in skill_tree:
            position = skill_sequence.get(s, -1)
            
            if position >= 0:
                # 현재 스킬의 순번이 이전 스킬의 순번과 2이상 차이나는 경우
                # 불가능한 스킬트리
                if position - previous_skill_position > 1:
                    is_available = False
                    break
                else:
                    previous_skill_position = position
            
        if is_available:
            count += 1

    return count
    