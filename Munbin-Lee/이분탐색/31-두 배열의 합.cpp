#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  vector<int> subSequenceSums[2];

  int t;
  cin >> t;

  for (auto &subSequenceSum: subSequenceSums) {
    int n;
    cin >> n;
    vector<int> v(n);
    subSequenceSum.reserve(n * (n + 1) / 2);

    for (int &j: v) {
      cin >> j;
    }

    for (int i = 0; i < n; i++) {
      int sum = 0;
      for (int j = i; j < n; j++) {
        sum += v[j];
        subSequenceSum.emplace_back(sum);
      }
    }
  }
  
  sort(subSequenceSums[1].begin(), subSequenceSums[1].end());

  long answer = 0;
  
  for (int i: subSequenceSums[0]) {
    int target = t - i;
    auto ub = upper_bound(subSequenceSums[1].begin(), subSequenceSums[1].end(), target);
    auto lb = lower_bound(subSequenceSums[1].begin(), subSequenceSums[1].end(), target);
    answer += ub - lb;
  }

  cout << answer;

  return 0;
}
