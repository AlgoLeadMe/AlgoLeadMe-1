import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b, c) = br.readLine().split(" ").map { it.toLong() }

    println(program(number = a, times = b, divider = c))
}

private fun program(number: Long, times: Long, divider: Long): Long {
    if (times == 1L) {
        return number % divider
    }
    if (times % 2 == 0L) {
        val temp = program(number, times / 2, divider)
        return (temp * temp) % divider
    }
    val temp = program(number, (times - 1) / 2, divider)
    return (temp * temp % divider * number) % divider
}
