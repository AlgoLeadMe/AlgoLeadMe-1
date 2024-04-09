import sys

def input(): return sys.stdin.readline().rstrip()

# 재귀함수 fr_check 
def fr_check(friend, stack):
    stack.append(friend)  # 현재 친구를 스택에 추가
    print(stack)

    if len(stack) == 5: # 친구 5명 되면 
        return stack

    for x in friends[friend]:
        if x not in stack:
            result = fr_check(x, stack.copy()) # 복사해야 별도의 stack이 만들어져서 전달 가능
            if result is not None:
                return result

    return None # stack이 5가 되지 않은 경우


N, M = map(int, input().split())
friends = [[] for _ in range(N)] #freind[i]에는 i의 친구 담기
fcheck = 0
stack = []


for _ in range(M):
    f0, f1 = map(int, input().split())
    friends[f0].append(f1)
    friends[f1].append(f0)


for idx in range(N):
    stack = []
    result = fr_check(idx, stack) #idx부터 체크 시작
    if result != None and len(result) == 5:
        fcheck = 1
        print("1")
        break

if fcheck == 0:
    print(0)