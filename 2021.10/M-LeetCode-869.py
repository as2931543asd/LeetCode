import collections


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = collections.Counter(str(n))
        for i in range(32):
            if c == collections.Counter(str(2 ** i)):
                return True
        return False
