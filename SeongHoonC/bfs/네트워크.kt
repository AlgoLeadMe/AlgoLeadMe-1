class 네트워크 {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        // 각 컴퓨터 방문했는지 확인
        val visited = BooleanArray(n){false}
        var count = 0

        for(i in 0 until n){
            // 이미 방문한 곳이라면 skip
            if(visited[i]){
               continue 
            }
            // 처음 방문한 곳이면 네트워크 + 1
            count++

            // i 인덱스에서 갈 수 있는 곳 모두 탐색
            val queue = ArrayDeque<Int>().apply { add(i) }
            while(queue.isNotEmpty()) {
                val com = queue.removeFirstOrNull() ?: -1
                val row = computers[com]
                
                for(j in 0 until n) {
                    if(row[j]==1 && !visited[j]) {
                       queue.add(j)
                       visited[j] = true
                    }
                }
            }
        }
        return count
    }
}