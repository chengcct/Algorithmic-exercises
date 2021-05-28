from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for i in "!?;',.":
            paragraph = paragraph.replace(i, ' ')
            list = paragraph.split()
        count = 0
        for j in set(list):
            s = list.count(j)
            if s > count and j not in banned:
                count = list.count(j)
                res = j
        return res


ret = Solution()
print(ret.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
