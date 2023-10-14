from copy import deepcopy

def solution(cards):
    answer = 0
    cards = list(map(lambda x : [cards.index(x),x],cards))

    for card1_with_index in cards:
        idx_card1, card1 = card1_with_index[0], card1_with_index[1]
        visited = [False for _ in range(len(cards))]
        left_cards = deepcopy(cards)
        
        temp = [card1_with_index]
        group1 = [card1]
        visited[idx_card1] = True
        left_cards.remove(card1_with_index)
        
        while temp:
            now_card_with_index = temp.pop()
            now_index, now_card = now_card_with_index[0], now_card_with_index[1]
            
            next_card_with_index = cards[now_card-1]
            next_index, next_card = next_card_with_index[0], next_card_with_index[1]
            
            if now_card_with_index != next_card_with_index:
                group1.append(next_card)
            
            if next_card_with_index in left_cards:
                left_cards.remove(next_card_with_index)
            
            if visited[next_card-1] == True:
                break
                
            else:
                temp.append(next_card_with_index)
                visited[now_card-1] = True        
        
        for card2_with_index in left_cards:
            idx_card2, card2 = card2_with_index[0], card2_with_index[1]
        
            temp = [card2_with_index]
            group2 = [card2]
            visited[idx_card2] = True
            
            while temp:
                now_card_with_index = temp.pop()
                now_index, now_card = now_card_with_index[0], now_card_with_index[1]
                
                next_card_with_index = cards[now_card-1]
                next_index, next_card = next_card_with_index[0], next_card_with_index[1]
                if now_card_with_index != next_card_with_index:
                    group2.append(next_card)
                
                if visited[next_card-1] == True:
                    break
                    
                else:
                    temp.append(next_card_with_index)
                    visited[now_card-1] = True
            
            answer = max(answer, len(group1)*len(group2))
    return answer