def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    count = 0

    while start <= end:
        count += 1
        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1
        else: # limit 초과 시 무거운 사람 한 명(end)만 태운다
            end -= 1

    return count