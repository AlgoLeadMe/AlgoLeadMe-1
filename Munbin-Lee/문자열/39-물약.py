stdin = open(0)

def input():
    return stdin.readline().rstrip()

N, M = map(int, input().split())

prices = {}

for _ in range(N):
    item, price = input().split()
    prices[item] = int(price)

recipes = []

for _ in range(M):
    target, formula = input().split('=')
    terms = formula.split('+')
    recipes.append([target, terms])

def updatePrice(target, terms):
    price = 0
    
    for term in terms:
        count = int(term[0])
        item = term[1:]
        
        if item not in prices:
            return
        
        price += count * prices[item]
    
    if target not in prices or prices[target] > price:
        prices[target] = price

for _ in range(M):
    for recipe in recipes:
        updatePrice(recipe[0], recipe[1])

if 'LOVE' not in prices:
    print('-1')
    exit()

answer = min(prices['LOVE'], 1000000001)
print(answer)
