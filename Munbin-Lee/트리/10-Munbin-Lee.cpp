#include <iostream>
#include <vector>
#include <set>

using namespace std;
using ll = long long;
using Range = pair<ll, ll>;

// second를 기준으로 키를 지정한다.
auto cmp = [] (const Range &a, const Range &b) {
    return a.second < b.second;
};

set<Range, decltype(cmp)> ranges(cmp);

void safeInsert(ll a, ll b) {
    if (a > b) return;
    ranges.insert({a, b});
}

ll checkIn(ll number) {
    // upper_bound(x)는 x를 초과하는 제일 작은 값을 탐색한다.
    // number 이상을 탐색하기 위해 키를 number-1로 지정하였다.
    auto it = ranges.upper_bound({0, number - 1});
    
    ll a = it->first, b = it->second;
    
    // 범위를 쪼갠다.
    ranges.erase(it);
    ll target = max(a, number);
    safeInsert(a, target - 1);
    safeInsert(target + 1, b);
    
    return target;
}

vector<ll> solution(ll k, vector<ll> numbers) {
    ranges.insert({1, k});
    vector<ll> answer;
    answer.reserve(numbers.size());

    for (ll number : numbers) {
        answer.emplace_back(checkIn(number));
    }

    return answer;
}