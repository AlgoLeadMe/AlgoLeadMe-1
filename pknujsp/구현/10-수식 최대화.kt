class Solution {

    fun solution(expression: String): Long {
        val convertedExpression = expression.convert()
        // 연산자 집합 추출
        val operators =
                convertedExpression.filter { it !is Long }.map { it as Long.(Long) -> Long }.toSet()
        val combinations = operators.combinations(emptyList())
        var maxReward = 0L

        // 조합 중에서 최댓값 파악
        for (combination in combinations) {
            maxReward = maxOf(maxReward, convertedExpression.calculate(combination))
        }
        return maxReward
    }

    // 연산자를 연산자 함수로 변경하고, 피연산자는 Long으로 변경후 목록 반환
    fun String.convert(): List<Any> {
        val operatorMap: Map<Char, Long.(Long) -> Long> =
                mapOf('-' to Long::minus, '+' to Long::plus, '*' to Long::times)
        val operators = filter { it in operatorMap }.map { operatorMap[it]!! }
        val expression = mutableListOf<Any>()

        replace('+', '-').replace('*', '-').split("-").also { operands ->
            for (i in 0 until operands.size - 1) {
                expression.add(operands[i].toLong())
                expression.add(operators[i])
            }
            expression.add(operands[operands.lastIndex].toLong())
        }
        return expression
    }

    // 조합생성
    fun Set<Long.(Long) -> Long>.combinations(
            list: List<Long.(Long) -> Long>
    ): List<List<Long.(Long) -> Long>> {
        if (isEmpty()) {
            return listOf(list)
        }

        val combinations = mutableListOf<List<Long.(Long) -> Long>>()
        for (op in this) {
            val newSet = toMutableSet()
            newSet.remove(op)
            combinations.addAll(newSet.combinations(list.plusElement(op)))
        }
        return combinations
    }

    fun List<Any>.calculate(operators: List<Long.(Long) -> Long>): Long {
        val expression = toMutableList()
        // 연산자별로 계산
        for (opr in operators) {
            // 중복 피연산자 검사 집합
            val checkedOperandIndexSet = mutableSetOf<Int>()
            // 피연산자맵, 피연산자의 위치와 피연산자의 목록
            val operandMap = mutableMapOf<Int, MutableList<Long>>()

            var operandIndex: Int
            var beginOperandIndex: Int = 0

            // 연산자의 위치는 홀수이므로 홀수만 확인
            for (operatorIndex in 1 until expression.size step 2) {
                if (expression[operatorIndex]!! != opr) {
                    continue
                }
                // A + B에서 피연산자 A,B와 각각의 위치를 함께 맵에 추가
                operandIndex = operatorIndex - 1

                // 좌측 피연산자 확인, 이미 확인한 피연산자이면 추가X
                if (operandIndex !in checkedOperandIndexSet) {
                    operandMap[operandIndex] = mutableListOf(expression[operandIndex]!! as Long)
                    beginOperandIndex = operandIndex
                }

                // 우측 피연산자 확인, 연산자 위치 바로 다음 위치에 있으므로 중복우려X
                operandMap[beginOperandIndex]!!.add((expression[operatorIndex + 1]!! as Long))
                checkedOperandIndexSet.add(operatorIndex + 1)
            }
            var removeLength: Int
            var result = 1L

            // 피연산자를 연산하고, 계산식에 값을 업데이트
            for (beginOperandIndex in operandMap.keys.reversed()) {
                operandMap[beginOperandIndex]!!.let { operands ->
                    // 연산한 피연산자는 식에서 제거한다
                    // A + B + C - D
                    // + 연산시 A위치에 계산 결과를 저장한다.
                    // (A + B + C) - D
                    removeLength = (operands.size - 1) * 2
                    repeat(removeLength) { expression.removeAt(beginOperandIndex) }

                    result = operands.first()
                    for (i in 1..operands.lastIndex) {
                        result = result.opr(operands[i])
                    }
                    expression[beginOperandIndex] = result
                }
            }
        }

        return Math.abs(expression.first() as Long)
    }
}
