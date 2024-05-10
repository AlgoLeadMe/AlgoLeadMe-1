import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val nums = br.readLine().split(" ").map { it.toInt() }
    val addedSum = Array(n + 1) { 0 }
    addedSum[1] = nums[0]

    // i 까지 누적합 구하기
    for (i in 2..n) {
        addedSum[i] = addedSum[i - 1] + nums[i - 1]
    }

    // 누적합 end 에서 누적합 start - 1 를 빼서 start ~ end 구간 합 구하기
    for (i in 0 until m) {
        val (start, end) = br.readLine().split(" ").map { it.toInt() }
        bw.write((addedSum[end] - addedSum[start - 1]).toString())
        bw.newLine()
    }
    // BufferedWriter 로 한번에 출력
    bw.flush()
    bw.close()
}
