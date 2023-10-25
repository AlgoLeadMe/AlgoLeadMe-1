#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

int solution(vector<int> money) {
    int n = money.size();
    array<vector<int>, 3> memo;
    memo[0] = {money[0], -1, money[0] + money[2]};
    memo[1] = {-1, money[1], -1};
    memo[2] = {-1, -1, money[2]};
    for (auto &m : memo) {
        m.resize(n);
    }
    
	for (int i = 3; i < n; i++) {
		for (int j = 0; j < 3; j++) {
			memo[j][i] = -1;
			
			if (memo[j][i - 2] != -1) {
				memo[j][i] = max(memo[j][i], memo[j][i - 2] + money[i]);
			}
			
			if (memo[j][i - 3] != -1) {
				memo[j][i] = max(memo[j][i], memo[j][i - 3] + money[i]);
			}
		}
	}
    
    int answer = max({
        memo[0][n - 3],
        memo[0][n - 2],
        memo[1][n - 2],
        memo[1][n - 1],
        memo[2][n - 2],
        memo[2][n - 1]
    });
    
    return answer;
}