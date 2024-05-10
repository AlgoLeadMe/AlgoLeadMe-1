class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {

        val answer = mutableListOf<Int>()
        val deque = ArrayDeque<Int>()

        repeat(progresses.size) {
            deque.add(작업일_계산(progresses[it], speeds[it]))
        }

        var max = deque.removeFirst()
        var count = 1

        while (deque.isNotEmpty()) {
            val now = deque.removeFirst()

            if (now <= max) {
                count++
                continue
            }
            max = now
            answer.add(count)
            count = 1
        }
        answer.add(count)
        return answer.toIntArray()
    }

    private fun 작업일_계산(숫자: Int, 나눌_것: Int): Int {
        var share = (100 - 숫자) / 나눌_것
        val rest = (100 - 숫자) % 나눌_것
        if (rest > 0) share += 1
        return share
    }
}
