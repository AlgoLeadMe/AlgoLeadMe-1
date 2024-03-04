#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    if (unordered_set<char>(s.begin(), s.end()).size() == 1) {
        cout << "-1";
        return 0;
    }

    auto isPalindrome = [](string &s) {
        int lo = 0;
        int hi = s.size() - 1; // NOLINT

        while (lo < hi) {
            if (s[lo] != s[hi]) return false;
            lo++;
            hi--;
        }

        return true;
    };

    if (!isPalindrome(s)) {
        cout << s.size();
        return 0;
    }

    cout << s.size() - 1;

    return 0;
}
