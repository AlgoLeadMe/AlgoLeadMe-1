private lateinit var letters: List<String>

fun main() {
    val br = System.`in`.bufferedReader()
    val (l, c) = br.readLine().split(" ").map { it.toInt() }
    letters = br.readLine().split(" ").sorted()

    for (i in 0..c - l) {
        dfs(i, letters[i], l)
    }
}

private fun dfs(index: Int, word: String, l: Int) {
    if (word.length == l) {
        val counts = "aeiou".toList().count { word.contains(it) }
        if (counts > 0 && l - counts > 1) {
            println(word)
        }
        return
    }
    for (i in index + 1 until letters.size) {
        dfs(i, word + letters[i], l)
    }
}