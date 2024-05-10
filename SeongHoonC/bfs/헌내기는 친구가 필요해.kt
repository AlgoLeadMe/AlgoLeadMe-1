import java.io.BufferedReader
import java.io.InputStreamReader

val dx = listOf(1, -1, 0, 0)
val dy = listOf(0, 0, 1, -1)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    // n * m graph
    val graph = Array(n) { Array(m) { "" } }
    var start: Pair<Int, Int> = Pair(-1, -1)
    for (i in 0 until n) {
        val line = br.readLine().toList().map { it.toString() }
        for (j in line.indices) {
            graph[i][j] = line[j]
            if (line[j] == "I") {
                start = Pair(i, j)
            }
        }
    }

    // n * m visited
    val visited = Array(n) { Array(m) { false } }
    visited[start.first][start.second] = true

    // 큐 생성
    val q = ArrayDeque<Pair<Int, Int>>()
    q.add(start)

    var count = 0

    while (q.isNotEmpty()) {
        val now = q.removeFirst()
        for (i in 0..3) {
            val nextX = now.first + dx[i]
            val nextY = now.second + dy[i]

            // 캠퍼스 밖을 나간다
            if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                continue
            }
            // 이미 방문했거나 벽은 못감
            if (visited[nextX][nextY] || graph[nextX][nextY] == "X") {
                continue
            }
            // 사람이면 친구하기
            if (graph[nextX][nextY] == "P") {
                count++
            }
            // 방문 표시 후 큐에 추가
            visited[nextX][nextY] = true
            q.add(Pair(nextX, nextY))
        }
    }
    println(if (count > 0) count else "TT")
}