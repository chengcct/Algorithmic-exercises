from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(1, row):
            for j in range(col):
                if j == 0:  # 左边界特殊情况
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j + 1]) + matrix[i][j]
                elif j == col - 1:  # 右边界特殊情况
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i - 1][j + 1]) + matrix[i][j]
        return min(matrix[-1])


ret = Solution()
print(ret.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
