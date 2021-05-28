class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curCup = [poured]
        for i in range(query_row):
            nextCup = [0] * (1 + len(curCup))
            for j in range(len(curCup)):
                if curCup[j] > 1:
                    nextCup[j] += (curCup[j] - 1) / 2
                    nextCup[j + 1] += (curCup[j] - 1) / 2
            curCup = nextCup
        return min(curCup[query_glass], 1)


ret = Solution()
print(ret.champagneTower(2, 1, 1))
