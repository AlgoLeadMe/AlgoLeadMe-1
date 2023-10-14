#include <string>
#include <vector>

using namespace std;

size_t n;
vector<vector<int>> memo;

int dp(int r, int c, const vector<vector<int>> &triangle) {
    int &m = memo[r][c];
    if (m != -1) return m;
    return m = triangle[r][c] +
        max(dp(r + 1, c, triangle), dp(r + 1, c + 1, triangle));
}

int solution(vector<vector<int>> triangle) {
    n = triangle.size();
    memo.resize(n, vector<int>(n, -1));
    for (int i = 0; i < n; i++) {
        memo[n - 1][i] = triangle[n - 1][i];
    }
    return dp(0, 0, triangle);
}