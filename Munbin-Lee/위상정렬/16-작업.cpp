#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> costs, times;
vector<vector<int>> parents;

int dfs(int x) {
    if (times[x]) return times[x];

    int time = 0;

    for (int parent: parents[x]) {
        time = max(time, dfs(parent));
    }

    time += costs[x];
    return times[x] = time;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    costs.resize(N + 1);
    times.resize(N + 1);
    parents.resize(N + 1);

    for (int i = 1; i <= N; i++) {
        int numParent;
        cin >> costs[i] >> numParent;
        while (numParent--) {
            int parent;
            cin >> parent;
            parents[i].emplace_back(parent);
        }
    }

    int answer = 0;

    for (int i = 1; i <= N; i++) {
        answer = max(answer, dfs(i));
    }

    cout << answer;

    return 0;
}
