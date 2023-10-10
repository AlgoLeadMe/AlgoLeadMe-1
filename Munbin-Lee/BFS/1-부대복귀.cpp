#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    // 간선 정보를 변형하여 저장
    
    vector<vector<int>> paths(n + 1);
    
    for (auto& road : roads) {
        int a = road[0];
        int b = road[1];
        paths[a].emplace_back(b);
        paths[b].emplace_back(a);
    }
    
    // BFS
    
    vector<int> costs(n + 1, -1);
    costs[destination] = 0;
    
    queue<pair<int, int>> q;
    q.emplace(destination, 0);
    
    while (!q.empty()) {
        auto [start, cost] = q.front();
        q.pop();
        cost++;
        for (int end : paths[start]) {
            if (costs[end] != -1) continue;
            costs[end] = cost;
            q.emplace(end, cost);
        }
    }
    
    // 정답 저장
    
    vector<int> answer;
    answer.reserve(sources.size());
    
    for (int source : sources) {
        answer.emplace_back(costs[source]);
    }
    
    return answer;
}