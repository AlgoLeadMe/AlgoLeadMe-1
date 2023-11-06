def solution(nums): 

 select = len(nums)/2
 types = len(set(nums)) 

 if select > types: 
   return types 
 else: 
   return select