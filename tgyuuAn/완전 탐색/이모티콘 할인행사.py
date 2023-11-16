from itertools import product

def solution(users, emoticons):
    
    emoticons_price_sale_list = []
    percent_list = [10,20,30,40]
    
    for temp in product(percent_list, repeat = len(emoticons)):
        emoticons_price_sale_list.append(temp)
        
    max_subscriber = -1
    max_earn_money = -1
    for emoticons_price_sale in emoticons_price_sale_list:
        
        temp_subscriber = 0
        temp_earn_money = 0
        for want_sale_percent, limit_price in users:
            
            temp_sum = 0
            for sale_percent, price in zip(emoticons_price_sale,emoticons):
                
                if sale_percent >= want_sale_percent:
                    temp_sum += price*(100-sale_percent)/100
                    
            if temp_sum >= limit_price:
                temp_subscriber += 1
                
            else:
                temp_earn_money += temp_sum
                
        if temp_subscriber > max_subscriber:
            max_subscriber = temp_subscriber
            max_earn_money = temp_earn_money
            
        elif temp_subscriber == max_subscriber and max_earn_money < temp_earn_money:
            max_earn_money = temp_earn_money

    return [max_subscriber, int(max_earn_money)]