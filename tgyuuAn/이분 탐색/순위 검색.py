from collections import defaultdict

def binary_search(arr, start, end, target):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start
    
def solution(infos, queries):
    answer = []
    cases = defaultdict(list)
                    
    for info in infos:
        info = info.split()
        for lan in [info[0], '-']:
            for job in [info[1], '-']:
                for career in [info[2], '-']:
                    for food in [info[3], '-']:
                        cases[lan+' '+job+' '+career+' '+food].append(int(info[4]))
    
    for key in cases.keys():
        cases[key].sort()
        
    for query in queries:
        query = query.split(' and ')
        query[3], score = query[3].split()
        scores = cases[query[0]+' '+query[1]+' '+query[2]+' '+query[3]]
        answer.append(len(scores)-binary_search(scores, 0, len(scores), int(score)))
        
    return answer