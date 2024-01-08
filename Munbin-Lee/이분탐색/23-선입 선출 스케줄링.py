def solution(n, cores):
    def get_works(time):
        works = 0

        for core in cores:
            works += time // core + 1

        return works
    
    lo = 1
    hi = 250_000_000
    
    while lo != hi:
        md = (lo + hi) // 2
        
        if get_works(md) >= n:
            hi = md
        else:
            lo = md + 1
    
    total_time = lo
    works_done = 0
    
    for core in cores:
        works_done += (total_time - 1) // core + 1
    
    for index, core in enumerate(cores):
        works_done += (total_time % core == 0)
        if works_done >= n: return index + 1