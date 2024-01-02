#include <iostream>
#include <vector>
#include <queue>

using namespace std;
using pr = pair<int, int>;

constexpr int INF = 987654321;

int N, M, S, D;
vector<vector<pr>> paths;
vector<int> minCosts;
vector<vector<int>> indegrees;
vector<vector<bool>> visited;

int dijkstra() {
    minCosts.assign(N, INF);
    minCosts[S] = 0;
    indegrees.assign(N, {});
    priority_queue<pr, vector<pr>, greater<>> pq;
    pq.emplace(0, S);

    while (!pq.empty()) {
        auto [cost, cur] = pq.top();
        pq.pop();

        for (auto [ncost, next]: paths[cur]) {
            if (visited[cur][next]) continue;

            ncost += cost;

            if (ncost > minCosts[next]) continue;

            if (ncost == minCosts[next]) {
                indegrees[next].emplace_back(cur);
                continue;
            }

            indegrees[next] = {cur};
            minCosts[next] = ncost;
            pq.emplace(ncost, next);
        }
    }

    int answer = minCosts[D];
    if (answer == INF) answer = -1;

    return answer;
}

void backtrack(int cur = D) {
    for (int prev: indegrees[cur]) {
        if (visited[prev][cur]) continue;
        visited[prev][cur] = true;
        backtrack(prev);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> S >> D;

    while (N != 0) {
        paths.assign(N, {});
        visited.assign(N, vector<bool>(N));

        while (M--) {
            int U, V, P;
            cin >> U >> V >> P;
            paths[U].emplace_back(P, V);
        }

        dijkstra();

        backtrack();

        cout << dijkstra() << '\n';

        cin >> N >> M >> S >> D;
    }

    return 0;
}