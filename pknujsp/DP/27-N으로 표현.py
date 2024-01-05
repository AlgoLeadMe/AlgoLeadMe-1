def solution(N, number):
    if N == number:
        return 1

    dp = [None, {N}]

    for count in range(2, 9):
        nums = {int(str(N) * count)}

        for i in range(1, count):
            for left in dp[i]:
                for right in dp[count - i]:
                    nums.add(left + right)
                    nums.add(left - right)
                    nums.add(left * right)

                    if right != 0:
                        nums.add(left // right)

        if number in nums:
            return count

        dp.append(nums)

    return -1
