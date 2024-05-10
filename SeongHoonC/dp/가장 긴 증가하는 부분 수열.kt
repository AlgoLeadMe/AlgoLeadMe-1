import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val arr = br.readLine().split(" ").map { it.toInt() }

    val answer = Array(n) { 1 }

    for (now in 1 until n) {
        for (target in 0 until now) {
            if (arr[target] < arr[now]) {
                answer[now] = max(answer[now], answer[target] + 1)
            }
        }
    }
    println(answer.max())
}