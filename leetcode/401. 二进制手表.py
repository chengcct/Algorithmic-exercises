from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']
        ans, clock = [], [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def dfs(i, num, hour, mins):
            if num == turnedOn:
                ans.append('{}:{:0>2d}'.format(hour, mins))
                return
            for j in range(i, 10):
                if j < 4:
                    if hour + clock[j] < 12:
                        dfs(j + 1, num + 1, hour + clock[j], mins)
                else:
                    if mins + clock[j] < 60:
                        dfs(j + 1, num + 1, hour, mins + clock[j])

        dfs(0, 0, 0, 0)
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.readBinaryWatch(1))
