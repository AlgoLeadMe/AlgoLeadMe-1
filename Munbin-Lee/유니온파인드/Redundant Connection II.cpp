class Solution {
public:
    vector<int> parents, roots;

    int find(int x) {
        if (x == roots[x]) return x;

        return roots[x] = find(roots[x]);
    }

    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        parents.resize(n + 1, -1);
        roots.resize(n + 1);
        iota(roots.begin(), roots.end(), 0);

        int hasDoubleParents = -1;
        array<int, 2> doubleParents;
        vector<int> cycle;

        for (auto &edge : edges) {
            int u = edge[0];
            int v = edge[1];

            // parent가 2개인 경우
            if (parents[v] != -1){
                hasDoubleParents = v;
                doubleParents = {parents[v], u};
                parents[v] = -1;
                continue;
            }

            parents[v] = u;

            // 사이클인 경우
            if (find(u) == find(v)) {
                cycle = {u, v};
                continue;
            }
            
            roots[v] = u;
        }

        if (hasDoubleParents == -1) return cycle;

        if (cycle.empty()) return {doubleParents[1], hasDoubleParents};

        return {doubleParents[0], hasDoubleParents};
    }
};