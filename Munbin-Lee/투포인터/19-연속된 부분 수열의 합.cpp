#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    int n = sequence.size();
    int lo = 0;
    int hi = 0;
    int cur = sequence[0];
    int minDist = 987654321;
    vector<int> answer;
    
    while (true) {
        if (cur == k) {
            int dist = hi - lo + 1;
            if (dist < minDist) {
                minDist = dist;
                answer = {lo, hi};
            }
            cur -= sequence[lo];
            lo++;
            if (++hi == n) break;
            cur += sequence[hi];
            continue;
        }
        
        if (cur < k) {
            if (++hi == n) break;
            cur += sequence[hi];
            continue;
        }
        
        if (cur > k) {
            cur -= sequence[lo];
            lo++;
        }
    }
    
    return answer;
}