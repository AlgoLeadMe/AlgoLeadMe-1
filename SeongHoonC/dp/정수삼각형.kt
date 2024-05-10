import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val triangle = Array(n + 1) { IntArray(n + 1) { 0 } }

    for (i in 1..n) {
        val input = br.readLine().split(" ").map { it.toInt() }
        for (j in 1..i) {
            triangle[i][j] = input[j - 1]
        }
    }

    for (i in 1..n) {
        for (j in 1..i) {
            triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j - 1], triangle[i - 1][j])
        }
    }
    println(triangle[n].max())
}
