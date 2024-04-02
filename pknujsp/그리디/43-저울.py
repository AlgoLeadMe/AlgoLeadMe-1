N = int(input())
weights = list(map(int, input().split()))
weights.sort()

x = 0
for weight in weights:
    # x + 1이 현재 추의 무게보다 작다면, 측정이 불가능함
    if x + 1 < weight:
        break

    x += weight

print(x + 1)