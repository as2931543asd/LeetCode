from typing import List


class Solution:
    # dp 当前状态和之前两个状态有关，取前一个状态或前两个状态和当前数组值的和中的最大值
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[1], nums[0])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return max(dp)
