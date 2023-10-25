def solution(n, l, r):
    return recursion(n,r) - recursion(n,l-1)


def recursion(n,pos):
    if n==1:
        return "11011"[:pos].count("1")
    
    quotient,remainder = divmod(pos, 5**(n-1))
    count = 0
    if quotient <= 1:
        count = 4**(n-1) * quotient + recursion(n-1,remainder)
        
    if quotient == 2:
        count = 4**(n-1) * quotient
        
    if quotient > 2:
        count = 4**(n-1) * (quotient-1) + recursion(n-1,remainder)
        
    return count