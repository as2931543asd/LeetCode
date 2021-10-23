# 2021年10月22日
from typing import List


# 暴力求解
# TODO 使用摩尔投票法优化空间复杂度
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        ans = []

        for v in nums:
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        for item in cnt.keys():
            if cnt[item] > len(nums) // 3:
                ans.append(item)

        return ans
