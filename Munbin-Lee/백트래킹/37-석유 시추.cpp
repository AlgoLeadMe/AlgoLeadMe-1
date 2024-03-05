#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

int solution(vector<vector<int>> land) {
    int r = land.size();
    int c = land[0].size();
    
    int dy[4] {-1, 0, 1, 0};
    int dx[4] {0, -1, 0, 1};
    
    vector<vector<int>> chunks(r, vector<int> (c, -1));
    vector<int> oils;
    
    auto bfs = [&](int y, int x, int chunk) {
        queue<pair<int, int>> q;
        q.emplace(y, x);
        
        int oil = 0;
        
        while (!q.empty()) {
            auto [cy, cx] = q.front();
            q.pop();

            oil++;
            chunks[cy][cx] = chunk;

            for (int dir = 0; dir < 4; dir++) {
                int ny = cy + dy[dir];
                int nx = cx + dx[dir];

                if (ny == -1 || ny == r || nx == -1 || nx == c) continue;
                if (land[ny][nx] == 0) continue;

                land[ny][nx] = 0;
                q.emplace(ny, nx);
            }
        }
        
        oils.emplace_back(oil);
    };
    
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            if (land[y][x] == 0) continue;
            
            land[y][x] = 0;
            bfs(y, x, oils.size());
        }
    }
    
    int answer = -1;
    
    for (int x = 0; x < c; x++) {
        unordered_set<int> set;
        
        for (int y = 0; y < r; y++) {
            int chunk = chunks[y][x];
            
            if (chunk == -1) continue;
            
            set.emplace(chunk);
        }
        
        int oil = 0;
        
        for (int chunk : set) {
            oil += oils[chunk];
        }
        
        answer = max(answer, oil);
    }
    
    return answer;
}
