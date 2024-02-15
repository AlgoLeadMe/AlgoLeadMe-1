#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int D, N;
    cin >> D >> N;

    stack<int> minOvens;
    int mn = 1087654321;

    while (D--) {
        int oven;
        cin >> oven;

        mn = min(mn, oven);
        minOvens.emplace(mn);
    }

    while (N--) {
        int pizza;
        cin >> pizza;

        while (!minOvens.empty() && minOvens.top() < pizza) {
            minOvens.pop();
        }

        if (!minOvens.empty()) {
            minOvens.pop();
        } else {
            cout << '0';
            return 0;
        }
    }

    cout << minOvens.size() + 1;

    return 0;
}