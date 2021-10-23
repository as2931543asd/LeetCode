from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(0)
        i = 0
        j = 1
        for num in nums:
            if num & 1 == 0:
                ans[i] = num
                i += 2
            else:
                ans[j] = num
                j += 2
        return ans
