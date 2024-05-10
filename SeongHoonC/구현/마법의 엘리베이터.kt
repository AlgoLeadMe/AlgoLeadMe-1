class `마법의 엘리베이터` {
    fun solution(storey: Int): Int {
        var number = storey
        var count = 0
        while (number > 0) {
            val remainder = number % 10
            when {
                remainder > 5 -> {
                    count += (10 - remainder)
                    number += 10
                }

                remainder < 5 -> count += remainder

                (number / 10) % 10 > 4 -> {
                    number += 10
                    count += remainder
                }

                else -> count += remainder
            }
            number /= 10
        }
        return count
    }
}