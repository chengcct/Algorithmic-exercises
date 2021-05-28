from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)  # 生成哈希表
        for i, j in enumerate(s):
            if dic[j] == 1:
                return i
        return -1


ret = Solution()
print(ret.firstUniqChar("loveleetcode"))
