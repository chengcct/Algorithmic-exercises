import itertools
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for j in words:
                if i in j and i != j:
                    res.append(i)
        return list(sorted(set(res)))


class Solution1:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [*{i for i, j in itertools.combinations(sorted(words, key=len), 2) if i in j}]


ret = Solution()
print(ret.stringMatching(["mass", "as", "hero", "superhero"]))
