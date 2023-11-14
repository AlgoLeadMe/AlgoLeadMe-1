def solution(sizes):
    w = []  
    h = [] 
    
    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])     
    
    return max(w) * max(h)