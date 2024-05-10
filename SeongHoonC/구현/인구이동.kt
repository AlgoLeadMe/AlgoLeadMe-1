import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayDeque
import kotlin.math.*

val dx = listOf(1, -1, 0, 0)
val dy = listOf(0, 0, 1, -1)
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, l, r) = br.readLine().split(" ").map { it.toInt() }
    val grounds = Array(n) { Array(n) { 0 } }

    for (i in 0 until n) {
        val line = br.readLine().split(" ").map { it.toInt() }
        for (j in 0 until n) {
            grounds[i][j] = line[j]
        }
    }
    var count = 0
    // 인구가 더이상 이동할 수 없을 때까지 반복
    while (moving(grounds, n, l, r)) {
        count++
    }
    println(count)
}

// L 명 이상 R 명 이하면 인구 이동하기
private fun moving(grounds: Array<Array<Int>>, n: Int, l: Int, r: Int): Boolean {
    val visited = Array(n) { Array(n) { false } }

    val unities = mutableListOf<List<Pair<Int, Int>>>()
    for (i in 0 until n) {
        for (j in 0 until n) {
            val unity = bfs(grounds, n, visited, i to j, l, r) ?: continue
            unities.add(unity)
        }
    }
    if (unities.isEmpty()) return false

    unities.forEach { goAverage(grounds, it) }

    return true
}

// 연합들을 평균값으로 변경
private fun goAverage(grounds: Array<Array<Int>>, unity: List<Pair<Int, Int>>) {
    val average = unity.sumOf { grounds[it.first][it.second] } / unity.size
    unity.forEach {
        grounds[it.first][it.second] = average
    }
}

// bfs 로 연합 다 찾기
private fun bfs(
    grounds: Array<Array<Int>>,
    n: Int,
    visited: Array<Array<Boolean>>,
    start: Pair<Int, Int>,
    l: Int,
    r: Int,
): List<Pair<Int, Int>>? {
    if (visited[start.first][start.second]) return null
    val deque = ArrayDeque<Pair<Int, Int>>()
    val unity = mutableListOf<Pair<Int, Int>>()
    deque.add(start)
    unity.add(start)
    visited[start.first][start.second] = true
    while (deque.isNotEmpty()) {
        val now = deque.removeFirst()
        for (i in 0..3) {
            val nextX = now.first + dx[i]
            val nextY = now.second + dy[i]
            if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= n) {
                continue
            }
            if (visited[nextX][nextY]) {
                continue
            }
            if (abs(grounds[nextX][nextY] - grounds[now.first][now.second]) !in l..r) {
                continue
            }
            visited[nextX][nextY] = true
            deque.add(nextX to nextY)
            unity.add(nextX to nextY)
        }
    }
    if (unity.size == 1) return null
    return unity
}
