#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool incentive(int x, const vector<vector<int>>& scores) {
    for (int i = 0; i < x; i++) {
        if (scores[x][0] < scores[i][0]
           && scores[x][1] < scores[i][1]) {
            return false;
        }
    }
    return true;
}

int solution(vector<vector<int>> scores) {
    pair<int, int> wanho = {scores[0][0], scores[0][1]};
    
    // 인센티브를 받지 못하는 경우
    
    for (auto& score : scores) {
        if (score[0] > wanho.first && score[1] > wanho.second) {
            return -1;
        }
    }
    
    // 점수 합 기준으로 내림차순 정렬
    
    sort(scores.begin(), scores.end(), [&wanho] (const auto &a, const auto &b) {
        if (a[0] + a[1] == b[0] + b[1]) {
            return a[0] != b[0] && a[0] == wanho.first;
        }
        return a[0] + a[1] > b[0] + b[1];
    });
    
    // 석차 판별
    
    int rank = 1;

    for (int i = 0; i < scores.size(); i++) {
        if (!incentive(i, scores)) continue;
        if (scores[i][0] == wanho.first
           && scores[i][1] == wanho.second) {
            return rank;
        }
        rank++;
    }
    
    return -1;
}