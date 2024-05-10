fun solution(picks: IntArray, minerals: Array<String>): Int {
    val tired = arrayOf(
        intArrayOf(1, 1, 1),
        intArrayOf(5, 1, 1),
        intArrayOf(25, 5, 1),
    )

    // 어차피 곡괭이 * 5 까지만 팔 수 있음, 뒤는 제거
    val groupSize = min(picks.sum(), (minerals.size / 5) + 1)
    val mineralGroups = Array(groupSize) { Array(5) { "" } }

    // 5개씩 그룹화한다.
    for (i in minerals.indices) {
        if (i / 5 >= groupSize) {
            break
        }
        mineralGroups[i / 5][i % 5] = minerals[i]
    }

    // 각 광물에 가중치를 줘서 그룹의 합계로 내림차순 정렬한다.
    mineralGroups.sortByDescending { group ->
        group.sumBy { mineral ->
            when (mineral) {
                "diamond" -> 25
                "iron" -> 5
                "stone" -> 1
                else -> 0
            }
        }
    }

    // queue 에 [3,1,2] 라면 0,0,0,1,2,2 가 들어감
    val queue = ArrayDeque<Int>()
    for (i in picks.indices) {
        repeat(picks[i]) {
            queue.add(i)
        }
    }

    // 곡괭이 하나당 5개씩 파내면서 피로도를 합계에 더한다
    var total = 0
    var nowIndex = 0

    while (queue.isNotEmpty()) {
        val pick = queue.removeFirst()
        // 곡괭이 pick 으로 각 광물 피로도 계산
        mineralGroups[nowIndex].forEach {
            val index = when (it) {
                "diamond" -> 0
                "iron" -> 1
                "stone" -> 2
                else -> -1
            }
            if (index != -1) {
                total += tired[pick][index]
            }
        }
        nowIndex++
        // 광물 다 팠으면 곧바로 종료
        if (nowIndex >= mineralGroups.size) {
            break
        }
    }
    return total
}
