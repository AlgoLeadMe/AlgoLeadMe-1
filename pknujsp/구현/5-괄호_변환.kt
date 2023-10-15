class Solution {
    val L = '('
    val R = ')'

    fun solution(p: String): String {
        return p.convert()
    }

    fun String.isValid(): Boolean {
        val stack = ArrayDeque<Char>()
        for (c in this) {
            if (c == L) {
                stack.add(c)
            } else {
                if (stack.isEmpty()) {
                    return false
                } else if (stack.removeLast() != L) {
                    return false
                }
            }
        }

        return stack.isEmpty()
    }

    fun String.convert(): String {
        if (isEmpty()) {
            return ""
        }

        val (u, v) =
                toList().let { splittedList ->
                    var lCount = 0
                    var rCount = 0

                    val uLastIndex =
                            splittedList.indexOfFirst {
                                if (it == L) lCount++ else rCount++

                                lCount == rCount
                            }

                    splittedList.subList(0, uLastIndex + 1).joinToString("") to
                            splittedList.subList(uLastIndex + 1, splittedList.size).joinToString("")
                }

        return if (u.isValid()) {
            "${u}${v.convert()}"
        } else {
            val sortedV = v.convert()
            val newU =
                    u.toList()
                            .subList(1, u.length - 1)
                            .map { if (it == L) R else L }
                            .joinToString("")

            "${L}${sortedV}${R}${newU}"
        }
    }
}
