from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur = 0
        for log in logs:
            if log.startswith('../'):
                cur -= 1
            elif log.startswith('./'):
                cur += 0
            else:
                cur += 1
            cur = cur if cur > 0 else 0
        return cur


ret = Solution()
print(ret.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
