# 2021年10月20日
from typing import List


# n-1个加一 = 一个元素-1
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
