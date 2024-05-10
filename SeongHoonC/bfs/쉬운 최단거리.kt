import java.io.BufferedReader
import java.io.InputStreamReader

val dx = listOf(1, -1, 0, 0)
val dy = listOf(0, 0, 1, -1)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    var start = 0 to 0
    val graph = Array(n) { Array(m) { 0 } }
    for (i in 0 until n) {
        val line = br.readLine().split(" ").map { it.toInt() }
        for (j in 0 until m) {
            if (line[j] == 2) {
                start = i to j
                graph[i][j] = 0
                continue
            }
            graph[i][j] = line[j]
        }
    }

    val q = ArrayDeque<Pair<Int, Int>>()
    val visited = Array(n) { Array(m) { false } }
    q.add(start)

    while (q.isNotEmpty()) {
        val now = q.removeFirst()

        for (i in 0..3) {
            val nextX = now.first + dx[i]
            val nextY = now.second + dy[i]

            if (nextX >= n || nextY >= m || nextX < 0 || nextY < 0) {
                continue
            }

            if (graph[nextX][nextY] == 0) {
                continue
            }

            if (visited[nextX][nextY]) {
                continue
            }

            graph[nextX][nextY] = graph[now.first][now.second] + 1
            visited[nextX][nextY] = true
            q.add(nextX to nextY)
        }
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            if (visited[i][j] || graph[i][j] == 0) {
                continue
            }
            graph[i][j] = -1
        }
    }

    for (i in 0 until n) {
        println(graph[i].joinToString(" "))
    }
}
