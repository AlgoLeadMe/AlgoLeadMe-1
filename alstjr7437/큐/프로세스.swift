import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var result = 0
    var priorities = priorities
    var location = location
    
    while priorities.count != 0 {
        location -= 1
        let p_max = priorities.max()!
        let temp = priorities[0]
        if p_max != temp {  // max가 아닐 경우(빼야할 경우가 아닌 경우)
            priorities.append(temp) // 뒤에 넣기
            priorities.removeFirst()    // 처음꺼 빼기
            if location < 0 {   // location이 음수면 제일 뒤에서 부터
                location = priorities.count - 1
            }
        } else {    // max일 경우(빼야할 경우)
            priorities.removeFirst()
            result += 1
            if location < 0 {   // location이 적절하게 오면 멈추기
                break
            }
        }
        
    }
    
    return result
}