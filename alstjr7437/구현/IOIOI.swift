let n = Int(readLine()!)!
let m = Int(readLine()!)!

let s = readLine()!.map{$0}

var result = 0
var cur = 0
var count = 0

while cur < m-2{
    if String(s[cur...cur + 2]) == "IOI"{
        count += 1
        cur += 2
        if count == n{
            result += 1
            count -= 1
        }
    } else {
        count = 0
        cur += 1
    }
}

print(result)


"""
50점짜리 코드

var p = "I" 
for _ in 0 ..< n{
    p += "OI"
}

for i in 0..<m-p.count+1{
    if String(s[i..<i+p.count]) == p{
        result += 1
    }
}
"""

