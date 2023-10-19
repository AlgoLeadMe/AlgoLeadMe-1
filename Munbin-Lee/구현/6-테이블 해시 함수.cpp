#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
	col--, row_begin--, row_end--;
    sort(data.begin(), data.end(), [col] (const auto &a, const auto &b) {
        if (a[col] == b[col]) return a[0] > b[0];
        return a[col] < b[col];
    });
    
    int answer = 0;
    for (int i = row_begin; i <= row_end; i++) {
        int s = 0;
        for (int j : data[i]) {
            s += j % (i + 1);
        }
        answer ^= s;
    }
    return answer;
}