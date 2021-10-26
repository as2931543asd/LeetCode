from typing import List


# 土味解法，遇到每个0就判断下能不能跳过去
# 从后往前，速度更快
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 2
        if n == 1:
            return True
        while i != -1:
            if nums[i] > 0:
                i -= 1
                continue
            for k in range(i - 1, -1, -1):
                if k + nums[k] > i:
                    i = k
                    break
            else:
                return False
        return True
