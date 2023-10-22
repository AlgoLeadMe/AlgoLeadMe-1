#include iostream
#include vector
#include algorithm

using namespace std;

int solution(vectorvectorint targets) {
    sort(targets.begin(), targets.end());
    int n = targets.size();
    int answer = 1;
    
    int mn = -1;
    int mx = 987654321;
    
    for (int i = 0; i  n; i++) {
        int s = targets[i][0];
        int e = targets[i][1];
        mn = max(mn, s);
        mx = min(mx, e);
        if (mx - mn = 0) {
            mn = -1;
            mx = 987654321;
            answer++;
            i--;
        }
    }
    
    return answer;
}