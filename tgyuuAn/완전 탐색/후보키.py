from itertools import combinations

def solution(relation):
    
    answer = 0
    len_row = len(relation)
    len_col = len(relation[0])
    candidate_key_set = set()
    
    for idx in range(1,len_col+1):
        for attributes_combination in combinations(range(len_col),idx):
            
            i_want_to_be_candidate_key_list = []
            for idx_row in range(len(relation)):
                
                temp_list = []
                for idx_col in attributes_combination:
                    temp_list.append(relation[idx_row][idx_col])
                
                if temp_list not in i_want_to_be_candidate_key_list:
                    i_want_to_be_candidate_key_list.append(temp_list)

            if len(i_want_to_be_candidate_key_list) == len_row:
                
                if len(candidate_key_set) == 0:
                    candidate_key_set.add(attributes_combination)
                    continue
                
                for candidate_key in candidate_key_set:
                    
                    count = 0
                    for candidate_element in candidate_key:
                        
                        if candidate_element not in attributes_combination:
                            break
    
                        elif candidate_element in attributes_combination:
                            count += 1
                    
                    if count == len(candidate_key):
                        break
                        
                    else:
                        continue
                        
                else:
                    candidate_key_set.add(tuple(attributes_combination))
                            
    return len(candidate_key_set)