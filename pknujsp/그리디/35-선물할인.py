from sys import *

n, budget, max_sales = map(int, stdin.readline().split())
gifts = sorted(list(map(int, stdin.readline().split())))

min_price_gift = max_price_gift = 0
prices = 0
sales = 0

for sale_gift in range(max_sales):
    prices += gifts[sale_gift] // 2
    max_price_gift += 1

    if prices > budget:
        print(sale_gift)
        exit()

sales = max_price_gift - min_price_gift
while max_price_gift < n:
    if sales < max_sales or max_sales == 0:
        if max_sales == 0:
            prices += gifts[max_price_gift]
        else:
            prices += gifts[max_price_gift] // 2

        if prices > budget:
            break

        max_price_gift += 1
        sales += 1
    else:
        prices += gifts[min_price_gift] // 2
        min_price_gift += 1
        sales -= 1

print(max_price_gift)
