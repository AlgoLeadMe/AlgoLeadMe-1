import sys

input = sys.stdin.readline

m = int(input())

result = 0

for _ in range(m):
    cmd = input().split()
    print(result)

    if cmd[0] == "add":
        result |= (1 << int(cmd[1]))

    if cmd[0] == "remove":
        result &= ~(1 << int(cmd[1]))

    if cmd[0] == "check":
        if result & (1 << int(cmd[1])):
            print(1)
        else:
            print(0)

    if cmd[0] == "toggle":
        result ^= (1 << int(cmd[1])) 

    if cmd[0] == "all":
        result = (1 << 21) - 1 

    if cmd[0] == "empty":
        result = 0 


# for _ in range(m):
#     cmd = input().split()

#     if cmd[0] == "add":
#         result[int(cmd[1])] = 1

#     if cmd[0] == "remove":
#         result[int(cmd[1])] = 0

#     if cmd[0] == "check":
#         if result[int(cmd[1])] == 1:
#             print(1)
#         else :
#             print(0)

#     if cmd[0] == "toggle":
#         if result[int(cmd[1])] == 1:
#             result[int(cmd[1])] = 0
#         else :
#             result[int(cmd[1])] = 1

#     if cmd[0] == "all":
#         result = [1] * len(result)

#     if cmd[0] == "empty":
#         result = [0] * len(result)

"""
S = set()

for _ in range(m):
    temp = input().split()
    
    if temp[0] == "add":
        S.add(int(temp[1]))
    if temp[0] == "remove":
        S.discard(int(temp[1]))
    if temp[0] == "check":
        if int(temp[1]) in S:
            print(1)
        else :
            print(0)
    if temp[0] == "toggle":
        if int(temp[1]) in S:
            S.discard(int(temp[1]))
        else:
            S.add(int(temp[1]))
    if temp[0] == "all":
        S = set([i for i in range(1, 21)])
    if temp[0] == "empty":
        S = set()
"""