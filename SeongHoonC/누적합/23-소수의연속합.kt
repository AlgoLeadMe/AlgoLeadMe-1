import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (head, tail) = 0 to 0
    val n = br.readLine().toInt()
    val primes = findPrimeNumbers(n)
    var count = 0

    while (head < primes.size && tail < primes.size) {
        val sum = primes.subList(head, tail + 1).sum()
        if (sum < n) {
            tail++
            continue
        }
        if (sum == n) {
            count++
        }
        head++
    }
    println(count)
}

private fun findPrimeNumbers(rangeMax: Int): List<Int> {
    return (2..rangeMax).filter {
        isPrime(it)
    }
}

private fun isPrime(num: Int): Boolean {
    for (i in 2..sqrt(num.toDouble()).toInt()) {
        if (num % i == 0) {
            return false
        }
    }
    return true
}
