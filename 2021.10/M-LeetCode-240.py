from typing import List


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for m in matrix:
#             for n in m:
#                 if n == target:
#                     return True
#                 elif n > target:
#                     break
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = 0
        m = len(matrix) - 1

        while n < len(matrix[0]) and m > -1:
            print(matrix[m][n])
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False


if __name__ == '__main__':
    c = Solution()
    print(c.searchMatrix([[-5]], -5))
