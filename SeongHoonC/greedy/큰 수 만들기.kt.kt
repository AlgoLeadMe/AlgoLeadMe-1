class Solution {
    fun solution(number: String, k: Int): String {
        var answer = StringBuilder()
        var index = 0

        // 각 자리의 가장 큰 수 구하기
        for (i in 0 until number.length - k) {
            var max = '0'
            // index 이후 큰 수 찾기
            for (j in index..i + k) {
                if (max < number[j]) {
                    max = number[j]
                    index = j + 1
                }
            }
            answer.append(max)
        }
        return answer.toString()
    }
}
