let N : String = readLine()!
var result : [Character:Int] = [:]

for i in N{
    let temp = (i == "9") ? "6" : i
    if result[temp] == nil{
        result[temp] = 1
    } else {
        result[temp]! += 1
    }
}
if result["6"] != nil{
    result["6"]! = (result["6"]! + 1) / 2
}

print(result.values.max() ?? 0)