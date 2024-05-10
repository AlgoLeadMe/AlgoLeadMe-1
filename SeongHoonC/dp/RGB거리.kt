import java.io.BufferedReader
import java.io.InputStreamReader

const val MAX = 987_654_321
val colors = 1..3
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val graph = Array(4) { Array(n + 1) { 0 } }
    val dp = Array(4) { Array(n + 1) { 0 } }
    for (i in 0 until n) {
        val line = br.readLine().split(" ").map { it.toInt() }
        for (j in 0..2) {
            graph[j + 1][i + 1] = line[j]
        }
    }

    // 각 집마다 현재 이 색을 칠할 때 최소값을 구한다
    for (houseIndex in 1..n) {
        for (colorIndex in colors) {
            dp[colorIndex][houseIndex] = colors.minOf {
                if (it == colorIndex) MAX else dp[it][houseIndex - 1] + graph[colorIndex][houseIndex]
            }
        }
    }
    println(colors.minOf { dp[it][n] })
}
