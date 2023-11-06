#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getRemovedWorks(const int maxWork, const vector<int> &works) {
    int res = 0;
    for (int work : works) {
        res += max(0, work - maxWork);
    }
    return res;
}

int binarySearch(const int n, const vector<int> &works) {
    int lo = 0;
    int hi = 50000;
    int res = 50000;
    int maxRemovedWorks = -1;
    
    while (lo <= hi) {
        int md = (lo + hi) / 2;
        int removedWorks = getRemovedWorks(md, works);
        if (removedWorks > n) {
            lo = md + 1;
        } else {
            if (removedWorks > maxRemovedWorks) res = md;
            hi = md - 1;
        }
    }
    return res;
}

long long solution(int n, vector<int> works) {
    int maxWork = binarySearch(n, works);
    n -= getRemovedWorks(maxWork, works);
    long answer = 0;
    for (int work : works) {
        work = min(work, maxWork);
        if (n && work && work == maxWork) {
            n--;
            work--;
        }
        answer += work * work;
    }
    return answer;
}