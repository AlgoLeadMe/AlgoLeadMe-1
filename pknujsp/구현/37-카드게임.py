def solution(coin, cards):
    a = set(cards[:len(cards) // 3])
    b = set()
    t = len(cards) + 1
    r = 1
    
    for i in range(len(cards) // 3 + 1, len(cards), 2):
        c1, c2 = cards[i - 1], cards[i]
        b.add(c1)
        b.add(c2)
        
        removed = False
        # 현재 가지고 있는 카드 목록 중 n + 1이 가능한 경우 확인
        for x in list(a):
            if t - x in a:
                a.remove(t - x)
                a.remove(x)
                removed = True
                break
        
        if removed:
            r += 1
            continue
            
        # 코인으로 교환해서 얻을 수 있는 카드 중에서 n + 1이 되는 경우를 찾아야 함
        # 코인이 없으므로 종료
        if not coin:
            break
            
        # `현재 갖고 있는 카드 + 얻을 수 있는 카드` = n + 1이 되는 경우를 확인
        for x in list(b):
            if t - x in a:
                a.remove(t - x)
                b.remove(x)
                removed = True
                coin -= 1
                break
        # 마지막 방법으로, 오직 교환으로 얻을 수 있는 카드 목록 중에서 n + 1이 되는 경우를 확인
        if not removed and coin >= 2:
            for x in list(b):
                if t - x in b:
                    b.remove(t - x)
                    b.remove(x)
                    removed = True
                    coin -= 2
                    break
        
        # n + 1을 어떤 경우에도 못 만들면 종료
        if not removed:
            break
        r += 1
        
    return r