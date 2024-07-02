import java.io.BufferedReader
import java.io.InputStreamReader

private var visited = mutableMapOf<Int, Int>()
private val lineMap: MutableMap<Int, List<Int>> = mutableMapOf()
private val stationMap: MutableMap<Int, List<Int>> = mutableMapOf()

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val queue = ArrayDeque<Int>()

    repeat(n) { line ->
        val input = br.readLine().split(" ").map { it.toInt() }
        val stations = input.subList(1, input.size)
        // 이 호선에서 갈 수 있는 곳
        lineMap[line + 1] = stations
        // 역에서 갈 수 있는 호선들
        stations.forEach { station -> stationMap[station] = stationMap.getOrDefault(station, listOf()) + (line + 1) }
        // 만약 출발(서울역) 을 포함하는 호선이면 바로 방문처리하고 큐에 넣기
        if (stations.contains(0)) {
            queue.addAll(stations)
            stations.forEach { station -> visited[station] = 0 }
        }
    }
    val target = br.readLine().toInt()

    // 이미 도착역을 방문했다면
    if (visited[target] != null) {
        println(0)
        return
    }

    while (queue.isNotEmpty()) {
        // 현재 역
        val now = queue.removeFirst()
        // 현재 역에서 갈 수 있는 호선에서 갈 수 있는 역들
        stationMap[now]!!.forEach { line ->
            lineMap[line]!!.forEach { station ->
                // 도착역이면
                if (station == target) {
                    println(visited[now]!! + 1)
                    return
                }
                // 방문한 적 없으면
                if (visited[station] == null) {
                    visited[station] = visited[now]!! + 1
                    queue.add(station)
                }
            }
        }
    }
    println(-1)
}
