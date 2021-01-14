#include<iostream>
#include<vector>
using namespace std;
class Djset {
public:
    vector<int> parent;  // 记录节点的根
    vector<int> rank;  // 记录根节点的深度（用于优化）
    Djset(int n): parent(vector<int>(n)), rank(vector<int>(n)) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool merge(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] < rank[rooty]) {
                swap(rootx, rooty);
            }
            parent[rooty] = rootx;
            if (rank[rootx] == rank[rooty]) rank[rootx] += 1;
            return false; // 根节点不同，返回false
            int i=0;
        }
        // 根节点相同，返回true
        return true;
    }
};
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        Djset ds(n);
        for (auto& e : edges) {
            if(ds.merge(e[0] - 1, e[1] - 1)) return {e[0],e[1]};
        }
        return {};
    }
};