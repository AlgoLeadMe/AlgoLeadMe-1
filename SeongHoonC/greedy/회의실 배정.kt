import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    var meets = mutableListOf<Pair<Int, Int>>()

    for (i in 0 until n) {
        val (x, y) = br.readLine().split(" ").map { it.toInt() }
        meets.add(x to y)
    }
    meets.sortWith(compareBy({ it.second }, { it.first }))

    var min = -1
    var count = 0
    for (i in meets.indices) {
        val meet = meets[i]
        // 회의 시작이 이미 시작한 회의보다 작으면 회의 못함
        if (meet.first < min) {
            continue
        }
        // 회의 끝이 최소값보다 작으면 갱신하고 +1
        if (meet.second > min) {
            min = meet.second
            count++
            continue
        }
        // 회의 시작과 끝이 같으면 +1
        if (meet.first == meet.second) {
            count++
        }
    }
    println(count)
}
