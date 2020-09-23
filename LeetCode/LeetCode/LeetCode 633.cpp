#include<math.h>
class Solution {
public:
    bool judgeSquareSum(int c) {
        long b = sqrt(c);
        long a = 0;
        long total = 0;
        while (a <= b) {
            total = a * a + b * b;
            if (total > c)
                b--;
            else if (total < c)
                a++;
            else
                return 1;
        }
        return 0;
    }
};