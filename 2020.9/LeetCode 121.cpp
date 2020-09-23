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
        // ��򵥵Ķ�̬�滮
        // ��¼����֮ǰ�������Сֵ
        // ����������󲢼�¼
        // ��������Сֵ
        for (size_t i = 0; i < prices.size(); i++)
        {
            Max = max(Max, prices[i] - Min);
            Min = min(prices[i], Min);
        }
        return Max;

    }
};