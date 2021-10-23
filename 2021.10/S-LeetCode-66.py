# 2021年10月21日
from typing import List

# 简单题 需要考虑进位的情况 因此需要统计末尾有多少个9 如果全是9 就额外加1 else 则在第一个不是9的位置加1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for j in range(len(digits)-1, -1, -1):
            if digits[j] == 9:
                digits[j] = 0
            else:
                digits[j] += 1
                return digits
        return [1] + digits