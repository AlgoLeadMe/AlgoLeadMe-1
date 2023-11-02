class Solution {
    val DELETE = "D"

    fun solution(operations: Array<String>): IntArray {
        val queue = ArrayDeque<Int>()
        var behavior: String
        var element: Int

        for (operation in operations) {
            operation.split(" ").run {
                behavior = this[0]
                element = this[1].toInt()
            }

            if (behavior == DELETE) {
                if (queue.isNotEmpty()) {
                    if (element == 1) {
                        // 최댓값 삭제
                        queue.removeLast()
                    } else {
                        // 최솟값 삭제
                        queue.removeFirst()
                    }
                }
            } else if (queue.isEmpty()) {
                queue.add(element)
            } else {
                if (queue.first() >= element) {
                    // 최솟값인 경우 맨 앞에 추가
                    queue.addFirst(element)
                } else if (queue.last() < element) {
                    // 최댓값인 경우 맨 끝에 추가
                    queue.addLast(element)
                } else {
                    // 중간 크기인 경우
                    for (i in queue.indices) {
                        if (element <= queue[i]) {
                            queue.add(i, element)
                            break
                        }
                    }
                }
            }
        }

        if (queue.isEmpty()) {
            queue.add(0)
            queue.add(0)
        }

        return intArrayOf(queue.last(), queue.first())
    }
}
