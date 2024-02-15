from sys import *

M, N = map(int, stdin.readline().split())
universes = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

planets_balance_dict = dict()

for i in range(M):
    planet_weights = sorted(set(universes[i]))
    order_dict = {planet: i for i, planet in enumerate(planet_weights)}
    order = tuple(order_dict[planet] for planet in universes[i])
    
    planets_balance_dict[order] = planets_balance_dict.get(order, 0) + 1

balanced_pairs_count = 0

for count in planets_balance_dict.values():
    if count == 1:
        continue
    balanced_pairs_count += count * (count - 1) // 2

print(balanced_pairs_count)
