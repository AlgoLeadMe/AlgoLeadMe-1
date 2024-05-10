class `블랙 사용자` {
    
    private var _bannedIds: Array<String> = arrayOf()
    private var answer = mutableSetOf<List<Int>>()
    
    fun solution(userIds: Array<String>, bannedIds: Array<String>): Int {
        _bannedIds = bannedIds
        dfs(userIds, 0, listOf())
        return answer.size
    }
    
    fun dfs(userIds: Array<String>, index: Int, usedIds: List<Int>) {
        if(index == _bannedIds.size ){
            answer.add(usedIds.sorted())
            return
        } 
        
        for(i in userIds.indices) {
            if(i in usedIds) {
                continue
            }
            if(!isBanned(userIds[i], _bannedIds[index])) {
                continue
            }
            dfs(userIds, index + 1, usedIds + i)
        }
    }
    
    private fun isBanned(userId: String, bannedId: String): Boolean {
        if(userId.length != bannedId.length){
            return false
        }
        for(i in userId.indices) {
            if(bannedId[i] == '*'|| userId[i] == bannedId[i]){
                continue
            }
            return false
        }
        return true
    }
}