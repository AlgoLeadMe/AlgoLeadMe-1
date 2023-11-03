def solution(column_length, row_length, puddles):
    if row_length == 1 or column_length == 1:
        return 1
    
    PUDDLE = -1
    MOD = 1_000_000_007
    row_length += 1
    column_length += 1

    paths = [[0] * column_length for _ in range(row_length)]
    paths[1][1] = 1
    
    for col, row in puddles:
        paths[row][col] = PUDDLE
                  
    for row in range(1, row_length):
        for col in range(1, column_length):
            if paths[row][col] == PUDDLE:
                paths[row][col] = 0
            else:
                left = paths[row][col-1]
                up = paths[row-1][col]
    
                paths[row][col] += (left + up)

    return paths[-1][-1] % MOD