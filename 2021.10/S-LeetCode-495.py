from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0: return 0  # 空集单独处理
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i - 1] + duration > timeSeries[i]:
                res += timeSeries[i] - timeSeries[i - 1]  # 状态转移
            else:
                res += duration
        res += duration  # 补足末位
        return res
