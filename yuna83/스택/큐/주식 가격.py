def solution(prices):
    length = len(prices)
   
    answer = [i for i in range(length - 1, -1, -1)] #마지막에서 처음까지 역순으로 반복
   
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j #주식이 떨어진 기간을 계산하여 저장
        stack.append(i) #주식 가격이 떨어지지 않은 상태에서 가장 최근에 나타난 주식 가격의 인덱스
 
    return answer