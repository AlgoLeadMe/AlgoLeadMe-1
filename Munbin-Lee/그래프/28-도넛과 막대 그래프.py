from collections import defaultdict

def solution(edges):
    indegrees = defaultdict(list)
    outdegrees = defaultdict(list)
    
    for begin, end in edges:
        outdegrees[begin].append(end)
        indegrees[end].append(begin)
    
    answer = [0] * 4
    
    for cur in outdegrees.keys():
        if len(indegrees[cur]) == 0 and len(outdegrees[cur]) >= 2:
            answer[0] = cur
            break
    
    def getGraphType(begin):
        if not outdegrees[begin]:
            return 2
        
        if len(outdegrees[begin]) != 1:
            return 3
        
        if outdegrees[begin][0] == begin:
            return 1
        
        visited = defaultdict(bool)
        visited[begin] = True
        
        cur = outdegrees[begin][0]
        visited[cur] = True
        
        while True:
            if not outdegrees[cur]:
                return 2
        
            if len(outdegrees[cur]) != 1:
                return 3
        
            cur = outdegrees[cur][0]
            
            if visited[cur]:
                return 1
            
            visited[cur] = True
    
    for outdegree in outdegrees[answer[0]]:
        graphType = getGraphType(outdegree)
        answer[graphType] += 1
    
    return answer