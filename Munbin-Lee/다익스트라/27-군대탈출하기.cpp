#include <iostream>
#include <vector>
#include <array>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> board(n, vector<int>(m));

    for (auto &row: board) {
        for (int &level: row) {
            cin >> level;
        }
    }

    const int INF = 1987654321;
    array<vector<vector<int>>, 2> minDists;
    minDists.fill(vector(n, vector<int>(m, INF)));
    minDists[false][0][0] = board[0][0];

    using tp = tuple<int, int, int, bool>;
    priority_queue<tp, vector<tp>, greater<>> pq;
    pq.emplace(board[0][0], 0, 0, false);

    const array<int, 4> dy = {-1, 0, 0, 1};
    const array<int, 4> dx = {0, -1, 1, 0};

    while (!pq.empty()) {
        auto [dist, cy, cx, skipped] = pq.top();
        pq.pop();

        for (int dir = 0; dir < 4; dir++) {
            int ny = cy + dy[dir];
            int nx = cx + dx[dir];

            if (ny == -1 || ny == n || nx == -1 || nx == m) continue;

            int ndist = max(dist, board[ny][nx]);

            if (ndist < minDists[skipped][ny][nx]) {
                minDists[skipped][ny][nx] = ndist;
                pq.emplace(ndist, ny, nx, skipped);
            }

            if (skipped) continue;

            int nny = ny + dy[dir];
            int nnx = nx + dx[dir];

            if (nny == -1 || nny == n || nnx == -1 || nnx == m) continue;

            int nndist = max(dist, board[nny][nnx]);

            if (nndist >= minDists[true][nny][nnx]) continue;

            minDists[true][nny][nnx] = nndist;
            pq.emplace(nndist, nny, nnx, true);
        }
    }

    cout << min(minDists[0][n - 1][m - 1], minDists[1][n - 1][m - 1]);

    return 0;
}