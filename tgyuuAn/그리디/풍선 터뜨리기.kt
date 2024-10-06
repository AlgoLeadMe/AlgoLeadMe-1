class Solution {
    fun solution(a: IntArray): Int {
        val _min = a.minOrNull() ?: return 0
        
        var ltrAnswer = 0
        var ltrPrevious = a[0]
        for((idx, ltrNum) in a.withIndex()){
            if(ltrNum == _min) break
            
            if(idx == 0) {
                ltrAnswer += 1
                continue
            }
            
            if(ltrPrevious > ltrNum){
                ltrAnswer += 1
                ltrPrevious = ltrNum
            }
        }
        
        var rtlAnswer = 0
        var rtlPrevious = a[a.size-1]
        for((idx, rtlNum) in a.reversed().withIndex()){
            if(rtlNum == _min) break

            if(idx == 0) {
                rtlAnswer += 1
                continue
            }
            
            if(rtlPrevious > rtlNum){
                rtlAnswer += 1
                rtlPrevious = rtlNum
            }
        }
        
        return ltrAnswer + rtlAnswer + 1
    }
}