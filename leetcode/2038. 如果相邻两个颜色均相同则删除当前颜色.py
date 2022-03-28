# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/22 17:34
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0
        if len(colors) < 3:
            return False
        for i in range(len(colors) - 2):
            if colors[i:i + 3] == 'AAA':
                count += 1
            elif colors[i:i + 3] == 'BBB':
                count -= 1
        return count > 0


if __name__ == '__main__':
    s = Solution()
    print(s.winnerOfGame('ABBBBBBBAAA'))
