#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long N;
    cin >> N;
    
    vector<bool> isPrime(N + 1, true);
    vector<long> prefixSum {0};
    long sum = 0;
    
    for (long i = 2; i <= N; i++) {
        if (!isPrime[i]) continue;
        
        sum += i;
        prefixSum.emplace_back(sum);
        
        for (long j = i * i; j <= N; j+= i) {
            isPrime[j] = false;
        }
    }
    
    int lo = 0;
    int hi = 1;
    int answer = 0;
    
    while (hi < prefixSum.size()) {
        long sum = prefixSum[hi] - prefixSum[lo];
        
        if (sum < N) {
           hi++;
           continue;
        }
        
        if (sum == N) {
            lo++;
            hi++;
            answer++;
            continue;
        }
        
        lo++;
    }
    
    cout << answer;
    
    return 0;
}