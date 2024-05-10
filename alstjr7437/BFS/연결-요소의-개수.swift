import Foundation

let input = readLine()!.split(separator:
                            " ").map{ Int($0)!}

let n = input[0] , m = input[1]

var graph : [[Int]] = Array(repeating: [], count: n + 1)
var visited : [Bool] = Array(repeating: false, count: n + 1)
var result : Int = 0

for _ in 0..<m {
    let tmp = readLine()!.split(separator: " ").map { Int($0)!}
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
}

func bfs(start: Int){
    visited[start] = true
    var queue: [Int] = [start]
    
    var idx : Int = 0
    
    while idx < queue.count{
        let current = queue[idx]
        
        idx += 1
        for i in graph[current]{
            if visited[i] == false {
                queue.append(i)
                visited[i] = true
            }
        }
    }
}

for i in 1...n{
    if visited[i] == false {
        bfs(start : i)
        result += 1
    }
}

print(result)