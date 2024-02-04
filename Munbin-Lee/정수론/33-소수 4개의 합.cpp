#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    auto isPrime = [](int x) {
        for (auto i = 2LL; i * i <= x; i++) {
            if (x % i == 0) return false;
        }

        return true;
    };

    auto solve = [&](int x) {
        string prefix;

        if (x & 1) {
            prefix = "2 3 ";
            x -= 5;
        } else {
            prefix = "2 2 ";
            x -= 4;
        }

        for (int i = 2; i <= x / 2; i++) {
            if (isPrime(i) && isPrime(x - i)) {
                cout << prefix << i << ' ' << x - i << '\n';
                return;
            }
        }

        cout << "Impossible.\n";
    };

    int N;

    while (cin >> N) {
        solve(N);
    }

    return 0;
}
