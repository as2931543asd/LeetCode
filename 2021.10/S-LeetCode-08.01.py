# class Solution:
#     def waysToStep(self, n: int) -> int:
#         # 动态规划
#         dp = [0, 1, 2, 4]
#         for i in range(4, n+1):
#             dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007)
#         return dp[n]
class Solution:
    def waysToStep(self, n: int) -> int:
        # 动态规划
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        a, b, c = 1, 2, 4
        for _ in range(4, n + 1):
            a, b, c = b, c, (a + b + c) % 1000000007
        return c
