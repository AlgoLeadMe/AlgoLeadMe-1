from collections import defaultdict

def solution(commands):
    table = [[None for _ in range(52)] for _ in range(52)]
    linked_dict = defaultdict(set)
    value_dict = defaultdict(set)
    answer = []
    
    for command in commands:
        splt = command.split()
        length = len(splt)
        query = splt[0]
        
        if query == "UPDATE":            
            if(length == 3):
                value1, value2 = splt[1], splt[2]

                temp = set()
                for (r, c) in value_dict[value1]:
                    table[r][c] = value2
                    temp.add((r,c))
                    
                value_dict[value1] = set()
                value_dict[value2].update(temp)
            
            elif(length == 4):
                r, c, value1 = int(splt[1]), int(splt[2]), splt[3]
                
                origin = table[r][c]         
                if len(linked_dict[(r,c)]) == 0:
                    table[r][c] = value1
                    value_dict[value1].add((r,c))
                    if origin is not None: value_dict[origin].discard((r,c))
                
                else:
                    for (l_r, l_c) in linked_dict[(r,c)]:
                        if origin is not None: value_dict[origin].discard((l_r, l_c))
                        table[l_r][l_c] = value1
     
                    value_dict[value1].update(linked_dict[(r,c)])

        elif query == "MERGE":
            r1, c1, r2, c2 = int(splt[1]), int(splt[2]), int(splt[3]), int(splt[4])
            
            if((r1, c1) == (r2, c2)): continue
            value1 = table[r1][c1]
            value2 = table[r2][c2]
            merge_value = None
            if value1 is not None and value2 is not None:
                merge_value = value1
                
            elif value1 is not None:
                merge_value = value1
                
            elif value2 is not None:
                merge_value = value2

            all_element = {(r1, c1), (r2, c2)}

            value1_element = {(r1, c1)} | linked_dict[(r1, c1)]
            value2_element = {(r2, c2)} | linked_dict[(r2, c2)]
            all_element = value1_element | value2_element
            
            if value1 is None and value2 is not None:
                for (el_r, el_c) in value1_element:
                    table[el_r][el_c] = merge_value

                    value_dict[value2].add((el_r, el_c))

            if not(value1 is None and value2 is None):
                for (el_r, el_c) in value2_element:
                    table[el_r][el_c] = merge_value

                    if value1 is not None and value2 is not None:
                        value_dict[value2].discard((el_r, el_c))
                        value_dict[value1].add((el_r, el_c))
                
                    elif value1 is not None:
                        value_dict[value2].discard((el_r, el_c))
                        value_dict[value1].add((el_r, el_c))

            for (l_r, l_c) in all_element:
                linked_dict[(l_r, l_c)] = all_element
                
        elif query =="UNMERGE":
            r, c = int(splt[1]), int(splt[2])
            value1 = table[r][c]
            value_dict[value1] -= linked_dict[(r, c)]

            for (now_r, now_c) in linked_dict[(r, c)]:
                linked_dict[(now_r, now_c)] = set()
                table[now_r][now_c] = None

            table[r][c] = value1
            value_dict[value1].add((r,c))

        elif query =="PRINT":
            r, c = int(splt[1]), int(splt[2])
            answer.append(table[r][c] if table[r][c] is not None else "EMPTY")

    return answer