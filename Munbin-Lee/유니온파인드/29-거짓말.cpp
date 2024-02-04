#include <iostream>
#include <vector>
#include <numeric>
#include <functional>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, numTruth;
    cin >> N >> M >> numTruth;
    
    vector<int> roots(N + 1);
    iota(roots.begin(), roots.end(), 0);
    
    function<int(int)> find = [&](int x) {
        if (roots[x] == x) return x;
        
        return roots[x] = find(roots[x]);
    };
    
    auto merge = [&](int a, int b) {
        a = find(a);
        b = find(b);
        
        if (a < b) swap(a, b);
        
        roots[a] = b;
    };
    
    while (numTruth--) {
        int truth;
        cin >> truth;
        
        merge(truth, 0);
    }
    
    vector<vector<int>> parties(M);
    
    for (auto& party : parties) {
        int numPeople;
        cin >> numPeople;
        
        while (numPeople--) {
            int person;
            cin >> person;
            
            party.emplace_back(person);
        }
    }
    
    for (auto& party : parties) {
        for (int person : party) {
            merge(person, party[0]);
        }
    }
    
    int answer = 0;
    
    for (auto& party : parties) {
        answer += (find(party[0]) != 0);
    }
    
    cout << answer;
    
    return 0;
}