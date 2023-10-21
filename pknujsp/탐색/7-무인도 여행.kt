class Solution {
    fun solution(maps: Array<String>): IntArray {
        return maps.find()
    }

    // BFS를 이용
    fun Array<String>.find(): IntArray {
        val rowLength = size
        val columnLength = this[0].length
        val x = 'X'
        val directions = arrayOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

        val checkedPoints = Array(rowLength) { BooleanArray(columnLength) }
        val queue = ArrayDeque<Pair<Int, Int>>()
        var point: Pair<Int, Int>

        var adjacentRowIndex: Int
        var adjacentColumnIndex: Int

        val numsOfDayToStay = mutableListOf<Int>()
        var numsOfDayToStayIndex = 0

        for ((rowIndex, row) in withIndex()) {
            for ((columnIndex, valueOfPoint) in row.withIndex()) {
                if (valueOfPoint == x || checkedPoints[rowIndex][columnIndex]) {
                    continue
                }

                numsOfDayToStay.add(valueOfPoint.digitToInt())
                checkedPoints[rowIndex][columnIndex] = true
                queue.add(rowIndex to columnIndex)

                while (queue.isNotEmpty()) {
                    point = queue.removeFirst()

                    for (direction in directions) {
                        adjacentRowIndex = point.first + direction.first
                        adjacentColumnIndex = point.second + direction.second

                        // 이동한 위치가 올바른 위치인지 확인
                        // 올바른 위치이고 x가 아니며 아직 방문하지 않은 위치인 경우 -> 큐에 추가하고 날짜 수를 더한다.
                        if (adjacentRowIndex >= 0 &&
                                        adjacentRowIndex < rowLength &&
                                        adjacentColumnIndex >= 0 &&
                                        adjacentColumnIndex < columnLength
                        ) {
                            if (this[adjacentRowIndex][adjacentColumnIndex] != x &&
                                            !checkedPoints[adjacentRowIndex][adjacentColumnIndex]
                            ) {
                                numsOfDayToStay[numsOfDayToStayIndex] +=
                                        this[adjacentRowIndex][adjacentColumnIndex].digitToInt()
                                checkedPoints[adjacentRowIndex][adjacentColumnIndex] = true
                                queue.add(adjacentRowIndex to adjacentColumnIndex)
                            }
                        }
                    }
                }

                numsOfDayToStayIndex++
            }
        }

        if (numsOfDayToStay.isEmpty()) {
            return intArrayOf(-1)
        }
        // 오름차순으로 정렬
        numsOfDayToStay.sort()
        return numsOfDayToStay.toIntArray()
    }
}
