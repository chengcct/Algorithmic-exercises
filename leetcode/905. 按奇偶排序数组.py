from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A


class Solution1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res1 = [i for i in A if i % 2 == 0]
        res2 = [i for i in A if i % 2 != 0]
        return res1 + res2


ret = Solution1()
print(ret.sortArrayByParity([3, 1, 2, 4]))
