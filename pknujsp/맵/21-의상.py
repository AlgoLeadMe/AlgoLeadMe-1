def solution(clothes):
    clothes_dict = {}

    for _, category in clothes:
        clothes_dict[category] = clothes_dict.get(category, 0) + 1

    result = 1
    for count in clothes_dict.values():
        result *= count + 1

    result -= 1
    return result
