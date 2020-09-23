#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1)
            return 0;
        int Min = prices[0], Max = 0;
        // 最简单的动态规划
        // 记录今天之前买入的最小值
        // 计算最大利润并记录
        // 并更新最小值
        for (size_t i = 0; i < prices.size(); i++)
        {
            Max = max(Max, prices[i] - Min);
            Min = min(prices[i], Min);
        }
        return Max;

    }
};