#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    const int MAX = 1'000'000;

    vector<int> f(MAX + 1);

    for (int i = 1; i <= MAX; i++) {
        for (int j = i; j <= MAX; j += i) {
            f[j] += i;
        }
    }

    vector<long> g(MAX + 1);

    for (int i = 1; i <= MAX; i++) {
        g[i] = g[i - 1] + f[i];
    }

    while (T--) {
        int N;
        cin >> N;

        cout << g[N] << '\n';
    }

    return 0;
}