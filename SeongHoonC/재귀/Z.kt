import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

var count = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, r, c) = br.readLine().split(" ").map { it.toInt() }
    programZ(n, 0, 0, r, c)
}

private fun programZ(n: Int, x: Int, y: Int, r: Int, c: Int) {
    val additionRange = 2.pow(n)
    // r 이나 c 가 포함된 부분이 아니라면 count 만 증가시키고 패스
    if (r !in x until x + additionRange || c !in y until y + additionRange) {
        count += additionRange * additionRange
        return
    }
    // n 이 0이 아니라면 4가지 범위로 나누어 Z 순으로 실행
    if (n != 0) {
        val additionIndex = 2.pow(n - 1)
        programZ(n - 1, x, y, r, c)
        programZ(n - 1, x, y + additionIndex, r, c)
        programZ(n - 1, x + additionIndex, y, r, c)
        programZ(n - 1, x + additionIndex, y + additionIndex, r, c)
        return
    }
    // n 이 0 이면 count 증가
    count++
    // x, y 가 r, c 면 출력
    if (x == r && y == c) {
        println(count)
    }
}

private fun Int.pow(n: Int) = this.toDouble().pow(n).toInt()
