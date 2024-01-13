#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> S(n);

    for (int &s: S) {
        cin >> s;
    }

    vector<int> answer, visited(50001);
    answer.reserve(n);

    for (int s: S) {
        if (visited[s] == 1) {
            answer.emplace_back(s + 1);
            continue;
        }

        if (s != 1 && visited[s - 1] == 0) {
            answer.emplace_back(s - 1);
            visited[s - 1] = 1;
            visited[s] = 2;
            continue;
        }

        answer.emplace_back(s);
        visited[s] = 1;
    }

    for (int i: answer) {
        cout << i << '\n';
    }

    return 0;
}