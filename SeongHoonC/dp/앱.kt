import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max
import kotlin.math.min

const val MAX_COST = 10_000
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    // 비용의 최대는 100 * 100 이다
    val dp = Array(n + 1) { Array(MAX_COST + 1) { 0 } }
    val bytes = listOf(0) + br.readLine().split(" ").map { it.toInt() }
    val cost = listOf(0) + br.readLine().split(" ").map { it.toInt() }

    var minCost = Int.MAX_VALUE
    for (i in 1..n) {
        for (j in 0..MAX_COST) {
            // 담을 수 없다면 이전에 i-1 까지 담아놓은 것 그대로
            if (j - cost[i] < 0) {
                dp[i][j] = dp[i - 1][j]
                continue
            }
            // 담을 수 있다면 현재 비용 - 앱의 비용 최적값에 얻을 수 있는 용량 더하기
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + bytes[i])

            // 목표 용량을 넘었다면 정답 최소값 업데이트
            if (dp[i][j] >= m) {
                minCost = min(minCost, j)
            }
        }
    }
    println(minCost)
}
