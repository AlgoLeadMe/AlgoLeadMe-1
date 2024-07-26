import java.io.BufferedReader
import java.io.InputStreamReader

private lateinit var br: BufferedReader
private lateinit var parents: Array<Int>

fun main() {
    br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    parents = Array(n + 1) { it }

    repeat(m) {
        val (command, a, b) = br.readLine().split(" ").map { it.toInt() }
        if (command == 0) {
            union(a, b)
        } else {
            println(if (findParents(a) == findParents(b)) "YES" else "NO")
        }
    }
}

private fun findParents(a: Int): Int {
    var parent = parents[a]
    while (parents[parent] != parent) {
        parent = parents[parent]
    }
    parents[a] = parent
    return parent
}

private fun union(a: Int, b: Int) {
    val parentA = findParents(a)
    val parentB = findParents(b)

    if (parentA == parentB) {
        return
    }
    if (parentA > parentB) {
        parents[parentA] = parentB
        return
    }
    parents[parentB] = parentA
}