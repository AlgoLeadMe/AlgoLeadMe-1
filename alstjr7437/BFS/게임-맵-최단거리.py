import Foundation

func solution(_ maps: [[Int]]) -> Int {
    var maps = maps
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, -1, 1]
    let rowCount = maps.count
    let colCount = maps[0].count
    
    func bfs(_ x: Int, _ y: Int) -> Int {
        var queue = [(x, y)]
        var index = 0
        
        while index < queue.count {
            let (x, y) = queue[index]
            index += 1
            
            for i in 0..<4 {
                let nx = x + dx[i]
                let ny = y + dy[i]
                
                if nx < 0 || nx >= rowCount || ny < 0 || ny >= colCount {
                    continue
                }
                
                if maps[nx][ny] == 0 {
                    continue
                }
                
                if maps[nx][ny] == 1 {
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                }
            }
        }
        
        return maps[rowCount - 1][colCount - 1]
    }
    
    let answer = bfs(0, 0)
    return answer == 1 ? -1 : answer
}

// 예시 호출
let maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]
print(solution(maps)) // 출력: 11