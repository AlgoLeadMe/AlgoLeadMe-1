#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> U(N);

    for (int &u: U) {
        cin >> u;
    }

    unordered_map<int, bool> sum;

    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            sum[U[x] + U[y]] = true;
        }
    }

    int answer = -1;

    for (int z = 0; z < N; z++) {
        for (int k = 0; k < N; k++) {
            if (U[k] <= answer) continue;
            if (!sum[(U[k] - U[z])]) continue;
            answer = U[k];
        }
    }

    cout << answer;

    return 0;
}
