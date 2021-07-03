from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        li = []
        for i, j in Counter(s).items():
            li.append([i, j])
        li1 = sorted(li, key=lambda x: -x[1])
        # print([i * j for i, j in li1])
        return ''.join([i * j for i, j in li1])


if __name__ == '__main__':
    res = Solution()
    print(res.frequencySort('tree'))
