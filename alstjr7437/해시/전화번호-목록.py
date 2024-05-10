# 1차 실패(시간 초과)
def solution(phone_book):
    for i in range(len(phone_book)):
        a = phone_book.pop(i)
        for j in phone_book:
            if a in j : 
                return False
        phone_book.insert(i, a)
    return True
    
# 2차 실패
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1] : 
            return False
    return True
    
# 최종
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

# hash를 이용
def solution(phone_book):
    hash = {}
    for i in phone_book:
        hash[i] = 1
    for i in phone_book:
        result = ""
        for j in i:
            result += j
            if result in hash and result != i:
                return False
    return True