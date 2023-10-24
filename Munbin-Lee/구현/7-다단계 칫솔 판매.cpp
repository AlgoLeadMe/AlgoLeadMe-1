#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void sell(int seller, int profits, vector<int> &answer, const vector<int> &parents) {
    int tax = profits * 0.1;
    answer[seller] += profits - tax;
    
    if (!tax || parents[seller] == -1) return;
    
    sell(parents[seller], tax, answer, parents);
}

vector<int> solution(vector<string> enroll, vector<string> referral,
                        vector<string> seller, vector<int> amount) {
    int n = enroll.size();
    unordered_map<string, int> indexs = {
        {"-", -1}
    };
    
    for (int i = 0; i < n; i++) {
        indexs[enroll[i]] = i;
    }
    
    vector<int> parents;
    parents.reserve(n);
    
    for (auto &parent : referral) {
        parents.emplace_back(indexs[parent]);
    }
    
    vector<int> answer(n);
    
    for (int i = 0; i < seller.size(); i++) {
        sell(indexs[seller[i]], amount[i] * 100, answer, parents);
    }
    
    return answer;
}