#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<string, int> map;

vector<int> solution(vector<string> gems) {
    int n = gems.size();
    
    for (auto &gem : gems) {
        map[gem] = 0;
    }
    
    int gemTypes = map.size();
    int lo = 0;
    int hi = -1;
    int currentGemTypes = 0;
    int minLen = 987654321;
    vector<int> answer = {1, 1};
    
    while (true) {
        
        // 모든 종류의 보석을 훔칠 때까지 hi++
        while (true) {
            if (hi == n - 1) break;
            hi++;
            map[gems[hi]]++;
            if (map[gems[hi]] == 1) currentGemTypes++;
            if (currentGemTypes == gemTypes) break;
        }
        
        if (currentGemTypes != gemTypes) break;
        
        // 모든 종류의 보석을 훔치지 못할 때까지 lo++
        while (true) {
            int len = hi - lo + 1;
            if (len < minLen) {
                minLen = len;
                answer[0] = lo + 1;
                answer[1] = hi + 1;
            }
            
            lo++;
            map[gems[lo - 1]]--;
            if (map[gems[lo - 1]] == 0) {
                currentGemTypes--;
                break;
            }
        }
    }
    
    return answer;
}