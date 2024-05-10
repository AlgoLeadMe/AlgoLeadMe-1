import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()

    val answer = Array(n) { 0 }
    val points = br.readLine().split(" ").map { it.toInt() }

    // index 와 함께 Pair 로 저장
    val indexedPoints = points.mapIndexed { index, i ->
        i to index
    }

    // 오름차순 정렬
    val sortedIndexedPoints = indexedPoints.sortedBy { it.first }

    var newIndex = -1
    var min = Int.MIN_VALUE

    // 작은 수 부터 0으로 새로운 좌표 부여
    sortedIndexedPoints.forEach {
        // 이전 수보다 더 큰 수면 최소값 업데이트, 좌표++
        if (min < it.first) {
            newIndex++
            min = it.first
        }
        // 본래 인덱스에 새로운 좌표값 넣기
        answer[it.second] = newIndex
    }

    println(arr.joinToString(" "))
}
