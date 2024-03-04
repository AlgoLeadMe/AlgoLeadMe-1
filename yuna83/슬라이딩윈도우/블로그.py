import sys
input=sys.stdin.readline

n,x=map(int,input().split())
data=list(map(int,input().split()))

if max(data) == 0:
    print("SAD")
else:
    value = sum(data[:x])  # x개씩 윈도우 생성
    max_value=value
    max_cnt=1

    for i in range(x,n):
        value+=data[i]
        value-=data[i-x]

        if value > max_value:
            max_value=value
            max_cnt =1

        elif value == max_value:
            max_cnt+=1

    print(max_value)
    print(max_cnt)