class Solution {
    val counts = intArrayOf(0, 0)
    val halfLengthMap: Map<Int, Int> = run {
        var exp = 1
        var previousExp: Int

        // 2거듭 제곱 수와 그의 절반을 미리 연산
        0.rangeTo(9).associate {
            previousExp = exp
            exp *= 2
            exp to previousExp
        }
    }

    fun solution(arr: Array<IntArray>): IntArray {
        arr.zip(0, 0, arr.size)
        return counts
    }

    fun Array<IntArray>.zip(row: Int, column: Int, length: Int) {
        val firstElement = this[row][column]

        // 모두 같은 값인지 확인
        var areSameValue = true
        val columnRange = (column) until (column + length)
        var arr: IntArray

        for (r in (row) until (row + length)) {
            arr = this[r]

            for (c in columnRange) {
                areSameValue = arr[c] == firstElement
                if (!areSameValue) {
                    break
                }
            }

            if (!areSameValue) {
                break
            }
        }

        // 0, 1만으로 이루어진 경우 0 또는 1의 개수를 증가시키고 리턴
        if (areSameValue) {
            counts[firstElement]++
            return
        }

        // 행렬 길이가 2이면 0,1의 개수를 증가시키고 리턴
        if (length == 2) {
            counts[firstElement]++
            counts[this[row][column + 1]]++
            counts[this[row + 1][column]]++
            counts[this[row + 1][column + 1]]++

            return
        }

        val halfLength = halfLengthMap[length]!!

        val centerRow = row + halfLength
        val centerColumn = column + halfLength

        val loopRanges =
                arrayOf(
                        row to column,
                        row to centerColumn,
                        centerRow to column,
                        centerRow to centerColumn
                )

        // 4 분할 한다
        for ((startRow, startColumn) in loopRanges) {
            zip(startRow, startColumn, halfLength)
        }
    }
}
