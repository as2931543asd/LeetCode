class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b, c = 0, 1, 1
        for i in range(2, n):
            a, b, c = b, c, b + c
        return c
