import sys
import itertools

def input() : return sys.stdin.readline().rstrip()

clothes = [["yellow_hat", "headgear"], 
           ["blue_sunglasses", "eyewear"], 
           ["green_turban", "headgear"],
           ["test1", "sample"],
           ["test2", "sample"],
           ]
c_dict = {}
answer = 1

for info in range(len(clothes)):
    if not clothes[info][1] in c_dict:
        c_dict[clothes[info][1]] = 1
    else:
        c_dict[clothes[info][1]] += 1

# answer = collections.Counter(c_dict)

for c in c_dict.values():
    answer *= (c+1)

answer -= 1

print(answer)
