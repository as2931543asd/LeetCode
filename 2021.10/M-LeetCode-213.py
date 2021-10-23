from typing import List


class Solution:
    # 将房子分为两块 在用rob1的思路分别处理已经分块的房子。最后取最大两边值就行
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        ans1 = self.my_split(nums[1:])
        ans2 = self.my_split(nums[:-1])
        return max(ans1, ans2)

    def my_split(self, nums: List[int]) -> int:
        dp = [nums[0], max(nums[1], nums[0])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return dp[-1]
