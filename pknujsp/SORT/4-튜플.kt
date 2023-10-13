class Solution {
    fun solution(s: String): IntArray {
        // s를 목록화 하였을떄 원소의 정규표현식
        val pattern = Regex("""\{{1,2}([0-9,]+)\}{1,2}""")
        val elements = pattern.findAll(s)
        val elementMap = mutableMapOf<Int, Int>()
        
        var v: Int
        var elementsSize: Int
        var lastV: Int?
        
        for(element in elements){
            element.groups[1]!!.value.split(",").run{
                elementsSize = size
                
                for(e in this){
                    v = e.toInt()
                    lastV = elementMap[v]
                    // 원소맵에 값이 있는 경우 -> 기존 값과 현재 원소목록의 크기 중 최솟값을 저장
                    // 값이 없으면 -> 현재 원소목록의 크기를 저장
                    elementMap[v] = if(lastV != null) minOf(elementsSize, lastV!!) else elementsSize
                }
            }
        }
        
        val tuple = IntArray(elements.count()) { 0 }
        elementMap.forEach{
            tuple[it.value - 1] = it.key
        }
        return tuple
    }
}