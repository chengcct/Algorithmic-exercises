from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for j in range(1, n):
            for i1 in range(j - 1, -1, -1):
                dp[i1][j] = max(piles[i1] - dp[i1 + 1][j], piles[j] - dp[j][j - 1])
        return dp[0][n - 1] > 0


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGame([3, 5, 4]))
