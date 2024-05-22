import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

val t1 = listOf(0 to 0, 0 to 1, 0 to 2, 0 to 3)
val t2 = listOf(0 to 0, 0 to 1, 1 to 0, 1 to 1)
val t3 = listOf(0 to 0, 1 to 0, 2 to 0, 2 to 1)
val t4 = listOf(0 to 0, 1 to 0, 1 to 1, 2 to 1)
val t5 = listOf(0 to 0, 0 to 1, 0 to 2, 1 to 1)
val tetrominos = listOf(t1, t2, t3, t4, t5)

private var n: Int = 0
private var m: Int = 0
private lateinit var board: Array<Array<Int>>
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val input = br.readLine().split(" ").map { it.toInt() }
    n = input[0]
    m = input[1]

    board = Array(n) { Array(m) { 0 } }
    // 숫자를 보드에 세팅
    repeat(n) {
        val line = br.readLine().split(" ").map { it.toInt() }
        line.forEachIndexed { index, value -> board[it][index] = value }
    }

    var maxTetromino = 0

    // 0,0 부터 n-1, m-1 까지 탐색
    for (x in 0 until n) {
        for (y in 0 until m) {
            tetrominos.forEach { tetromino ->
                // 그대로
                maxTetromino = max(maxTetromino, sumAllDirection(x, y, tetromino))
                // 뒤집어서
                maxTetromino = max(maxTetromino, sumAllDirection(x, y, tetromino.reverseTetromino()))
            }
        }
    }
    println(maxTetromino)
}

// 90도씩 회전시켜 최대값 return
private fun sumAllDirection(x: Int, y: Int, tetromino: List<Pair<Int, Int>>): Int {
    var maxTetromino = 0
    var nowTetromino = tetromino
    repeat(4) {
        maxTetromino = max(maxTetromino, sumTetromino(x, y, nowTetromino))
        nowTetromino = nowTetromino.translate()
    }
    return maxTetromino
}

// board 의 tetromino 숫자 합 계산
private fun sumTetromino(x: Int, y: Int, tetromino: List<Pair<Int, Int>>): Int {
    var sum = 0
    for (move in tetromino) {
        val nowX = x + move.first
        val nowY = y + move.second
        if (nowX >= n || nowY >= m || nowX < 0 || nowY < 0) {
            return -1
        }
        sum += board[nowX][nowY]
    }
    return sum
}

// tetromino 를 90도 회전
private fun List<Pair<Int, Int>>.translate() = map { it.second to -1 * it.first }

// tetromino 를 뒤집기
private fun List<Pair<Int, Int>>.reverseTetromino() = map { it.first to (it.second * -1) }
