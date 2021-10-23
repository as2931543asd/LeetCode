class Solution:
    # 滑动窗口 每次计算最大值和最小值的差异就行
    def minimumDifference(self, nums: list, k: int) -> int:
        nums.sort()
        min_ = nums[-1]
        for i in range(len(nums) - k+1):
            min_ = min(min_, nums[i+k-1] - nums[i])
        return min_
# test