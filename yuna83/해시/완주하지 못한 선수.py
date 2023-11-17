def solution(participant, completion):
    hashDict = {}
    sumHash = 0
   
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
       
    for comp in completion:
        sumHash -= hash(comp)
       
    return hashDict[sumHash]