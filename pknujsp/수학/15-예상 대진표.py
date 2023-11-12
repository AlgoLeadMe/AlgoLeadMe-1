def solution(N, A, B):
    A -= 1
    B -= 1
    round = 0

    while abs(A - B) >= 1:
        round += 1

        A //= 2
        B //= 2

    return round
