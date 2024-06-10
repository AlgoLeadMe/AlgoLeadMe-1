import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

private lateinit var br: BufferedReader

fun main() {
    br = BufferedReader(InputStreamReader(System.`in`))
    var minCount = 100_001
    val (n, s) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }
    var head = 0
    var tail = 1
    var sum = arr[head]
    while (true) {
        if (head >= arr.size) {
            break
        }
        // s 보다 크거나 같다면
        if (sum >= s && tail > head) {
            minCount = min(minCount, tail - head)
            sum -= arr[head]
            head++
            continue
        }
        // s 보다 작다면
        if (tail >= arr.size) break
        sum += arr[tail]
        tail++
    }
    println(if (minCount == 100_001) 0 else minCount)
}