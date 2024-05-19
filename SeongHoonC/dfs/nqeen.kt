import java.io.BufferedReader
import java.io.InputStreamReader

var answer = 0
var n: Int = 0
lateinit var board: IntArray
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    n = br.readLine().toInt()
    board = IntArray(n)
    backTracking(0)
    println(answer)
}

private fun backTracking(row: Int) {
    // row 가 증가하다가 n 이랑 같아지면 정답 +1
    if (row == n) {
        answer++
        return
    }
    // row 일 때 각 열에 놓을 경우의 수
    for (col in 0 until n) {
        board[row] = col
        // 놓을 수 있다면 다음 행
        if (check(row)) backTracking(row + 1)
    }
}

private fun check(row: Int): Boolean {
    for (i in 0 until row) {
        // 행이 같거나
        if (board[row] == board[i]) {
            return false
        }
        // 대각선
        if (row - i == kotlin.math.abs(board[row] - board[i])) {
            return false
        }
    }
    return true
}
