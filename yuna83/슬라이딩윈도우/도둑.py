import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    home=list(map(int,input().split()))

    if m!=n:
        for j in range(m-1):
            home.append(home[j])

    start= 0
    end=m-1
    count=sum(home[:m])
    answer=0

    if count<k: # 시작 윈도우 확인
        answer+=1
    while end<len(home)-1:
        count-=home[start]
        start+=1
        end+=1
        count+=home[end]
        if count<k:
            answer+=1
    print(answer)
