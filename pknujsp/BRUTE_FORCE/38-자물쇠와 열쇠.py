# 자물쇠의 중간 부분이 모두 1인지 확인
def is_valid(new_lock):
    length = len(new_lock) // 3
    
    for r in range(length, length * 2):
        for c in range(length, length * 2):
            if new_lock[r][c] != 1:
                return False
            
    return True

def solution(key, lock):
    n = len(lock)
    k = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for r in range(n):
        for c in range(n):
            new_lock[r + n][c + n] = lock[r][c]
            
    for _ in range(4):
        rev_key = key[::-1]
        key = []
        for c in range(k):
            row = []
            for r in range(k):
                row.append(rev_key[r][c])
            key.append(row)
        
        """
        열쇠를 돌리는 로직은 한 줄로도 구현가능 합니다
        key = [row for row in zip(*reversed(key))]
        """

        for r in range(n * 2):
            for c in range(n * 2):
                # 자물쇠에 열쇠를 끼운다
                for i in range(k):
                    for j in range(k):
                        new_lock[r + i][c + j] += key[i][j]
                        
                # 자물쇠에 열쇠가 딱 들어갔는지 확인
                if is_valid(new_lock):
                    return True
                
                # 자물쇠에서 열쇠를 빼서 복구시킨다
                for i in range(k):
                    for j in range(k):
                        new_lock[r + i][c + j] -= key[i][j]
    return False