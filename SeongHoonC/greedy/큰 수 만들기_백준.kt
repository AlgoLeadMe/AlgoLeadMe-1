import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val numbers = br.readLine().split(" ")
    val queue = PriorityQueue<Target>()
    numbers.forEach {
        queue.add(Target(it))
    }
    val stringBuilder = StringBuilder()
    while (queue.isNotEmpty()) {
        stringBuilder.append(queue.poll().number)
    }
    if (stringBuilder.all { it == '0' }) {
        println(0)
        return
    }
    println(stringBuilder.toString())
}

data class Target(val number: String) : Comparable<Target> {
    override fun compareTo(other: Target): Int {
        return if (number + other.number > other.number + number) -1 else 1
    }
}
