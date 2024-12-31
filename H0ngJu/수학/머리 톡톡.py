import sys

def input() : return sys.stdin.readline().rstrip()

N = int(input())
students = [int(input()) for _ in range(N)]
hits = [0 for _ in range(1000001)]
results = [0 for _ in range(N)]

for student in students:
    hits[student] += 1

for idx in range(len(students)):
    for i in range(1, int(students[idx]**(1/2)) + 1):
        if students[idx] % i == 0:
            results[idx] += hits[i]
            if (i ** 2) != students[idx]:
                results[idx] +=  hits[students[idx] // i]

for r in results:
    print(r-1, end=" ")