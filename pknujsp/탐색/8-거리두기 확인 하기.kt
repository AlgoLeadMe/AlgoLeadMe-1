class Solution {
    val P = 'P'
    val X = 'X'
    val directions = arrayOf(-1 to 0, 1 to 0, 0 to -1, 0 to 1)
    val dangerousDistanceRange = 1..2

    fun solution(places: Array<Array<String>>): IntArray {
        // 각 대기실에서 응시자가 앉아있는 자리의 위치를 목록화
        return places
                .map { room ->
                    room
                            .mapIndexed { rowIndex, row ->
                                row
                                        .mapIndexed { columnIndex, column -> columnIndex to column }
                                        .filter { type -> type.second == P }
                                        .map { person -> rowIndex to person.first }
                            }
                            .flatten()
                            .analysis(room)
                }
                .toIntArray()
    }

    // BFS
    fun List<Pair<Int, Int>>.analysis(room: Array<String>): Int {
        val queue: ArrayDeque<Triple<Int, Int, Int>> = ArrayDeque()

        // rowIndex, columnIndex, distance
        var point: Triple<Int, Int, Int>
        var adjPoint: Triple<Int, Int, Int>

        // 응시자 자리의 위치에서 시작하여 거리두기를 지키고 있는지 확인
        for ((pRowIndex, pColumnIndex) in this) {
            val checkedPositions = Array(5) { BooleanArray(5) }

            queue.add(Triple(pRowIndex, pColumnIndex, 0))
            checkedPositions[pRowIndex][pColumnIndex] = true

            while (queue.isNotEmpty()) {
                point = queue.removeFirst()

                // 현 위치가 다른 응시자의 위치이면서,
                // 거리가 2이하인 경우 거리두기를 지키지 않으므로 0을 반환
                if (room[point.first][point.second] == P && (point.third in dangerousDistanceRange)
                ) {
                    return 0
                }

                for (direction in directions) {
                    // 이동하고 거리 증가
                    adjPoint =
                            Triple(
                                    point.first + direction.first,
                                    point.second + direction.second,
                                    point.third + 1
                            )

                    // 이동한 위치가 유효한 위치인지 파악
                    // 유효하고 파티션이 있는 위치가 아니며 아직 확인하지 않은 곳인 경우
                    // 큐에 위치를 추가하고 방문처리
                    if (adjPoint.isValidPosition() &&
                                    !checkedPositions[adjPoint.first][adjPoint.second] &&
                                    room[adjPoint.first][adjPoint.second] != X
                    ) {
                        checkedPositions[adjPoint.first][adjPoint.second] = true
                        queue.add(adjPoint)
                    }
                }
            }
        }

        return 1
    }

    fun Triple<Int, Int, Int>.isValidPosition(): Boolean {
        return (first >= 0) && (first < 5) && (second >= 0) && (second < 5)
    }
}
