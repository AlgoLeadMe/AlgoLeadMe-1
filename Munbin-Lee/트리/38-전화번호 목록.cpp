#include <iostream>
#include <vector>

using namespace std;

struct Trie {
    struct Node {
        Node *children[10]{};
        bool isTerminal = false;
    };

    Node *root = new Node;

    bool insert(string &s) const {
        auto cur = root;

        for (char ch: s) {
            int digit = ch - '0';

            if (!cur->children[digit]) {
                cur->children[digit] = new Node();
                cur = cur->children[digit];
                continue;
            }

            if (cur->children[digit]->isTerminal) {
                return false;
            }

            cur = cur->children[digit];
        }

        for (auto child: cur->children) {
            if (child) {
                return false;
            }
        }

        cur->isTerminal = true;

        return true;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    auto solve = []() {
        auto trie = new Trie;

        int n;
        cin >> n;

        vector<string> numbers(n);

        for (auto &number: numbers) {
            cin >> number;
        }

        for (auto number: numbers) {
            if (!trie->insert(number)) {
                cout << "NO\n";
                delete trie;
                return;
            }
        }

        cout << "YES\n";
    };

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
