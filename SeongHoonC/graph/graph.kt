import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var graph: Array<Array<String>>
private lateinit var visited: Array<Array<Boolean>>
private lateinit var br: BufferedReader

val dx = listOf(1, 0, 0, -1)
val dy = listOf(0, 1, -1, 0)
val dD = listOf("D", "R", "L", "U")
val dDInverse = listOf("U", "L", "R", "D")
fun main() {
    br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    graph = Array(n) { Array(m) { "X" } }
    visited = Array(n) { Array(m) { false } }

    repeat(n) {
        val line = br.readLine().chunked(1)
        line.forEachIndexed { index: Int, s: String ->
            graph[it][index] = s
        }
    }
    var count = 0
    for (x in 0 until n) {
        for (y in 0 until m) {
            if (findSafeZone(x, y, n, m)) count++
        }
    }
    println(count)
}

// bfs 로 같은 사이클에 존재하는 애들 다 찾기
private fun findSafeZone(x: Int, y: Int, n: Int, m: Int): Boolean {
    if (visited[x][y]) return false
    val q = ArrayDeque<Pair<Int, Int>>()
    q.add(x to y)
    while (q.isNotEmpty()) {
        val now = q.removeFirst()
        val nowDirection = dD.indexOf(graph[now.first][now.second])
        for (i in 0..3) {
            val nextX = now.first + dx[i]
            val nextY = now.second + dy[i]
            // 범위 넘어감
            if (nextX >= n || nextY >= m || nextX < 0 || nextY < 0) continue
            if (visited[nextX][nextY]) continue
            // 이동 방향과 같을 때 or 현재 구역으로 이동할 곳
            if (dDInverse[i] == graph[nextX][nextY] || i == nowDirection) {
                visited[nextX][nextY] = true
                q.add(nextX to nextY)
            }
        }
    }
    return true
}
