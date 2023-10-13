class 프로그래머스_연속_부분_수열_합의_개수 {
    class Solution {
        fun solution(elements: IntArray): Int {
            val sumSet = mutableSetOf<Int>()
            var endIdx: Int
            val oversizedElements = elements + elements
            val indices = elements.indices

            for (count in 0 until elements.size) {
                endIdx = count
                indices.forEach { startIdx ->
                    endIdx++

                    var sum = 0
                    for (idx in startIdx until endIdx) {
                        sum += oversizedElements[idx]
                    }
                    sumSet.add(sum)
                }
            }

            return sumSet.size
        }
    }
}
