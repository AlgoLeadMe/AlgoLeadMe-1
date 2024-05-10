class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var count = 0
        val q = ArrayDeque<Int>()
        val map = mutableMapOf<Int, Int>()

        // 딕셔너리에 key 는 index 고 value 는 우선순위로 초기화한다.
        // queue 에 모든 index 를 순서대로 넣는다.
        for (i in priorities.indices) {
            q.add(i)
            map[i] = priorities[i]
        }

        // 우선순위의 최대값을 구한다.
        var max = q.maxOf { map[it]!! }
        
        // 큐에 남아있으면 반복한다.
        while (q.isNotEmpty()) {
            
            // 최대값보다 작다면 마지막에 추가
            // 최대값보다 크거나 같으면 count 를 증가시키고 우선순위 최대값을 업데이트한다.
            val now = q.removeFirst()
            if (map[now]!! < max) {
                q.add(now)
            } else {
                count++
                // location 과 같으면 반복을 종료
                if (now == location) {
                    break
                }
                max = q.maxOf { map[it]!! }
            }
        }
        
        // 마지막에 count 를 반환한다.
        return count
    }
}