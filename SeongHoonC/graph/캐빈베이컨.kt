import java.io.BufferedReader
import java.io.InputStreamReader

private const val INF = 987_654_321
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val graph = Array(n + 1) { i ->
        Array(n + 1) { j -> if (i == j) 0 else INF }
    }

    repeat(m) {
        val (a, b) = br.readLine().split(" ").map { it.toInt() }
        graph[a][b] = 1
        graph[b][a] = 1
    }

    for (k in 1..n) {
        for (i in 1..n) {
            for (j in 1..n) {
                if (graph[i][j] > graph[i][k] + graph[k][j]) {
                    graph[i][j] = graph[i][k] + graph[k][j]
                }
            }
        }
    }

    var min = INF
    var answer = -1

    for (i in 1..n) {
        val sum = (1..n).sumOf { j -> graph[i][j] }
        if (min > sum) {
            min = sum
            answer = i
        }
    }

    println(answer)
}
