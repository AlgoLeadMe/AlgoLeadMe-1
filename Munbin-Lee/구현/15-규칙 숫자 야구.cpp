#include <iostream>
#include <array>
#include <vector>

using namespace std;

int solve() {
	array<bool, 10> answerVisited {}, inputVisited {};
	
	char answer[5], input[5];
	cin >> answer >> input;
	
	for (int i = 0; i < 4; i++) {
		answer[i] -= '0';
		input[i] -= '0';
		answerVisited[answer[i]] = true;
		inputVisited[input[i]] = true;
	}
	
	for (int round = 1; ; round++) {
		// Correct
		for (int i = 0; i < 4; i++) {
			if (answer[i] != input[i]) break;
			if (i == 3) return round;
		}
		
		array<bool, 4> strikes{};
		bool anyBall = false;
		
		for (int i = 0; i < 4; i++) {
			// Strike
			if (answer[i] == input[i]) {
				strikes[i] = true;
				continue;
			}
			
			// Fail
			if (!answerVisited[input[i]]) {
				inputVisited[input[i]] = false;
				do {
					input[i]++;
					input[i] %= 10;
				} while (inputVisited[input[i]]);
				inputVisited[input[i]] = true;
				continue;
			}
			
			// Ball
			anyBall = true;
		}
		
		if (!anyBall) continue;
		
		vector<int> rotateTargets;
		
		for (int i = 0; i < 4; i++) {
			if (strikes[i]) continue;
			rotateTargets.emplace_back(i);
		}
		
		for (int i = rotateTargets.size() - 1; i - 1 >= 0; i--) {
			swap(input[rotateTargets[i - 1]], input[rotateTargets[i]]);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cout << solve();
	
	return 0;
}