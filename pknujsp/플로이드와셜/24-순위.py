def solution(n, results):
    matrix = [[False] * n for _ in range(n)]
    for a, b in results:
        matrix[a - 1][b - 1] = True
    
    for mid in range(n):
        for i in range(n):
            for j in range(n):
                if not matrix[i][j] and matrix[i][mid] and matrix[mid][j]:
                    matrix[i][j] = True

    target_weight = n - 1
    count = 0
    
    for v in range(n):
        outs = matrix[v].count(True)
        ins = 0
        
        for r in range(n):
            ins += matrix[r][v]
        
        if ins + outs == target_weight:
            count += 1

    return count