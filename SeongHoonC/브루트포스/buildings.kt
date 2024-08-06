import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

private lateinit var buildings: List<Int>

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var maxCount: Int = 0
    buildings = listOf(0) + br.readLine().split(" ").map { it.toInt() }
    for (now in 1..n) {
        maxCount = max(find(now, height = buildings[now], n), maxCount)
    }
    println(maxCount)
}

private fun find(now: Int, height: Int, n: Int): Int {
    var result = 0
    var minSlope = Double.MAX_VALUE
    for (i in now - 1 downTo 1) {
        val x = (height - buildings[i]).toDouble() / (now - i)
        if (x < minSlope) {
            minSlope = x
            result++
        }
    }

    var maxSlope: Double = -1234567899.0
    for (i in (now + 1)..n) {
        val slope = (buildings[i] - height).toDouble() / (i - now)
        if (slope > maxSlope) {
            maxSlope = slope
            result++
        }
    }
    return result
}
