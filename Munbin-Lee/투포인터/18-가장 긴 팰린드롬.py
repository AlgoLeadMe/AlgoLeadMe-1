def solution(s):
    n = len(s)
    
    def get_longest_palindrome(lo, hi):
        if hi == n or s[lo] != s[hi]: return 0
        
        while lo - 1 >= 0 and hi + 1 < n and s[lo - 1] == s[hi + 1]:
            lo -= 1
            hi += 1
        
        return hi - lo + 1
    
    answer = 0
    
    for i in range(n):
        answer = max(
            answer,
            get_longest_palindrome(i, i),
            get_longest_palindrome(i, i + 1)
        )

    return answer