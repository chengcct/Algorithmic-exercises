from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            word[tmp].append(i)

        return list(word.values())


if __name__ == '__main__':
    s = Solution()
    a = s.groupAnagrams(['asd', 'dsa'])
    print(a)


