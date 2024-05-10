import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.min

private const val INF = 987_654_321L
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val (N, E) = br.readLine().split(" ").map { it.toInt() }
    val graph = Array(N + 1) { mutableListOf<Pair<Int, Long>>() }
    for (i in 0 until E) {
        val (start, end, cost) = br.readLine().split(" ").map { it.toInt() }
        graph[start].add((end to cost.toLong()))
        graph[end].add((start to cost.toLong()))
    }

    val (v1, v2) = br.readLine().split(" ").map { it.toInt() }
    // 1 to v1 + v1 to v2 + v2 to N
    val cost1 = dijkstra(N, 1, v1, graph) + dijkstra(N, v1, v2, graph) + dijkstra(N, v2, N, graph)
    // 1 to v2 + v2 to v1 + v1 to N
    val cost2 = dijkstra(N, 1, v2, graph) + dijkstra(N, v2, v1, graph) + dijkstra(N, v1, N, graph)

    val answer = min(cost1, cost2)
    println(if (answer >= INF) -1 else answer)
}

// start to end 최단거리 구하기
private fun dijkstra(N: Int, start: Int, end: Int, graph: Array<MutableList<Pair<Int, Long>>>): Long {
    if (start == end) {
        return 0
    }
    val pq = PriorityQueue<Edge>()
    val distance = Array(N + 1) { INF }

    distance[start] = 0
    pq.add(Edge(start, 0))

    while (pq.isNotEmpty()) {
        val (now, dist) = pq.poll()
        for ((next, cost) in graph[now]) {
            val nextCost: Long = dist + cost
            if (distance[next] > nextCost) {
                distance[next] = nextCost
                pq.add(Edge(next, nextCost))
            }
        }
    }

    return distance[end]
}

data class Edge(val start: Int, val cost: Long) : Comparable<Edge> {

    // 거리(비용)가 짧은 것이 높은 우선순위를 가지도록 설정
    override operator fun compareTo(other: Edge): Int {
        return if (this.cost < other.cost) -1 else 1
    }
}
