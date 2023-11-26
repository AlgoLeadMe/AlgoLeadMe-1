# deque

from collections import *


def solution(people, limit):
    people = deque(sorted(people, reverse=True))

    count = 0
    while people:
        if people[0] + people[-1] <= limit:
            people.pop()

        if people:
            people.popleft()

        count += 1

    return count


# two pointer


def solution(people, limit):
    people.sort(reverse=True)

    count = 0
    heavy_idx = 0
    light_idx = len(people) - 1

    while heavy_idx <= light_idx:
        if people[heavy_idx] + people[light_idx] <= limit:
            light_idx -= 1

        heavy_idx += 1
        count += 1

    return count
