# class Solution:
#     def myAtoi(self, s: str) -> int:
#         import re
#         at_oi_re = re.compile('^[ ]*([+-]?\d+)')
#         if not at_oi_re.search(s):
#             return 0
#         res = int(at_oi_re.findall(s)[0])
#         return min(max(res, -2 ** 31), 2 ** 31 - 1)
import torch

transfer = torch.nn.Linear(256, 256)
theta = torch.randn([150, 256])
t = transfer(theta)
print(t)
t = torch.nn.functional.softmax(t, dim=0)
print(t)
