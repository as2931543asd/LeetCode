#include<iostream>
#include<vector>
using namespace std;

class Solution1 {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        vector<int> answer;
        int count = 0;
        for (size_t i = 0; i < A.size(); i++) {
            if (A[i] % 2 == 0)
                count += A[i];
        }
        for (int i = 0; i < queries.size(); i++) {
            if ((A[queries[i][1]] + queries[i][0]) % 2 == 0 && A[queries[i][1]] % 2 == 0) {
                A[queries[i][1]] += queries[i][0];
                count += queries[i][0];
            }
            else if ((A[queries[i][1]] + queries[i][0]) % 2 == 0 && A[queries[i][1]] % 2 != 0) {
                A[queries[i][1]] += queries[i][0];
                count += A[queries[i][1]];
            }
            else if ((A[queries[i][1]] + queries[i][0]) % 2 != 0 && A[queries[i][1]] % 2 == 0) {
                count -= A[queries[i][1]];
                A[queries[i][1]] += queries[i][0];
            }
            else
                A[queries[i][1]] += queries[i][0];
            answer.push_back(count);
        }
        return answer;
    }

};
