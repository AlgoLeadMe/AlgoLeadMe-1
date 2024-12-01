fun gcd(a: Int, b: Int): Int {
    var tempA = maxOf(a, b)
    var tempB = minOf(a, b)
    
    if(tempB <= 0){
        return 0
    }
    
    while (tempA % tempB >= 1){
        val tempC = tempA%tempB
        tempA = tempB
        tempB = tempC
    }
    
    return tempB
}

fun main() {
    val N = readln().toInt()
    val ratio = IntArray(N){ 1 }
    val linked = Array(N) { mutableListOf<Int>() }
    
    repeat(N-1){
        val info = readln().split(" ").map{ it.toInt() }
        val a = info[0]
        val b = info[1]
        var p = info[2]
        var q = info[3]
        val divGcd = gcd(p, q)
        p /= divGcd
        q /= divGcd
        
        // println("$a $b $p $q")
        
        val aLinked = mutableSetOf<Int>(a)
        val aDeq = ArrayDeque<Int>()
        aDeq.addFirst(a)
        while(!aDeq.isEmpty()){
            val now = aDeq.removeFirst()
            
            for(neighbor in linked[now]){
                if(neighbor in aLinked){
                    continue
                }
                
                aLinked.add(neighbor)
                aDeq.addLast(neighbor)
            }
        }
        
        val bLinked = mutableSetOf<Int>(b)
        val bDeq = ArrayDeque<Int>()
        bDeq.addFirst(b)
        while(!bDeq.isEmpty()){
            val now = bDeq.removeFirst()
            
            for(neighbor in linked[now]){
                if(neighbor in bLinked){
                    continue
                }
                
                bLinked.add(neighbor)
                bDeq.addLast(neighbor)
            }
        }
        
        // println("$aLinked $bLinked")
        
        val tempARatio = ratio[a]
        val tempBRatio = ratio[b]
        
        for(aNeighbor in aLinked){
            ratio[aNeighbor] *= (tempBRatio * p)
        }
        
        for(bNeighbor in bLinked){
            ratio[bNeighbor] *= (tempARatio * q)
        }
        
        linked[a].add(b)
        linked[b].add(a)
        
        // println(linked.toList().toString())
        // println(ratio.toList().toString())
        // println()
    }
    
    val allGcd = ratio.reduce(::gcd)
    for(elemIdx in 0 until ratio.size){
        ratio[elemIdx] /= allGcd
    }
    
    println(ratio.toList()
    .toString()
    .replace(",", "")
    .replace("[", "")
    .replace("]", ""))
}