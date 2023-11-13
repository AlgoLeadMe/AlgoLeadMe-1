KEY_PAD = {i + 1: (i // 3, i % 3) for i in range(9)}
KEY_PAD["*"] = (3, 0)
KEY_PAD[0] = (3, 1)
KEY_PAD["#"] = (3, 2)

LEFT_START = "*"
RIGHT_START = "#"


def distance(start_key, target_key):
    start = KEY_PAD[start_key]
    target = KEY_PAD[target_key]

    return abs(target[0] - start[0]) + abs(target[1] - start[1])


def solution(numbers, hand):
    left_handed = hand == "left"
    L, R = "L", "R"
    left_hand, right_hand = LEFT_START, RIGHT_START

    left_hand_only_keys = set([1, 4, 7])
    right_hand_only_keys = set([3, 6, 9])

    history = []

    for key in numbers:
        use_left_hand = False

        if key in left_hand_only_keys:
            use_left_hand = True
        elif key not in right_hand_only_keys:
            distance_from_left = distance(left_hand, key)
            distance_from_right = distance(right_hand, key)

            if distance_from_left == distance_from_right:
                use_left_hand = left_handed
            elif distance_from_left < distance_from_right:
                use_left_hand = True

        if use_left_hand:
            history.append(L)
            left_hand = key
        else:
            history.append(R)
            right_hand = key

    return "".join(history)
