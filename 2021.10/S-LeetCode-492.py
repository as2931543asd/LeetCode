# 2021年10月23日
from typing import List
from math import sqrt


# 因为W<=L,推出w<=sqrt(area)
# 从sqrt(area)开始找到第一个能被sqrt整除的数
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(sqrt(area))
        while area % W != 0:
            W -= 1
        L = area // W
        return [L, W]