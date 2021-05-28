from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        l = len(M)
        w = len(M[0])
        # 初始化平滑后矩阵
        N = [[0 for _ in range(w)] for _ in range(l)]
        for i in range(l):
            for j in range(w):
                f = 0
                count = 0
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if 0 <= q < w and 0 <= p < l:
                            f += M[p][q]
                            count += 1
                N[i][j] = f / count
        return N


class Solution1:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not (len(M) or len(M[0])):
            return M

        smoothedImage = []
        directions = [[-1, -1], [-1, 0], [-1, 1],
                      [0, -1], [0, 0], [0, 1],
                      [1, -1], [1, 0], [1, 1]]

        for x in range(len(M)):
            oneRow = []
            for y in range(len(M[0])):
                sum = 0
                count = 0
                # 计算有效邻居点的加权平均
                for direct in directions:
                    if 0 <= y + direct[0] < len(M[0]) and 0 <= x + direct[1] < len(M):
                        sum += M[x + direct[1]][y + direct[0]]
                        count += 1
                oneRow.append(sum // count)
            smoothedImage.append(oneRow)
        return smoothedImage


ret = Solution1()
print(ret.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
