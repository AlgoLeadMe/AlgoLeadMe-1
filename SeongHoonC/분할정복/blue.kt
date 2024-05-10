import java.io.BufferedReader
import java.io.InputStreamReader

var blue = 0
var white = 0
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val paper = Array(n) { Array(n) { 0 } }

    for (i in 0 until n) {
        val line = br.readLine().split(" ").map { it.toInt() }
        for (j in 0 until n) {
            paper[i][j] = line[j]
        }
    }

    cut(0, 0, n, paper)
    println(white)
    println(blue)
}

private fun cut(x: Int, y: Int, n: Int, paper: Array<Array<Int>>) {
    if (checkPaper(x = x, y = y, n = n, paper = paper, target = 1) { blue++ }) return
    if (checkPaper(x = x, y = y, n = n, paper = paper, target = 0) { white++ }) return

    val divN = n / 2
    cut(x, y, divN, paper)
    cut(x + divN, y, divN, paper)
    cut(x, y + divN, divN, paper)
    cut(x + divN, y + divN, divN, paper)
}

private fun checkPaper(x: Int, y: Int, n: Int, paper: Array<Array<Int>>, target: Int, action: () -> Unit): Boolean {
    val isSame = (x until x + n).all { dx -> (y until y + n).all { dy -> paper[dx][dy] == target } }
    if (isSame) {
        action()
        return true
    }
    return false
}