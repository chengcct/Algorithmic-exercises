from re import findall
from functools import reduce
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def cal(m, n):
            div1, divs1 = map(int, m.split('/'))
            div2, divs2 = map(int, n.split('/'))
            # 最小公倍数
            lcm = divs1 * divs2 // gcd(divs1, divs2)
            div = div1 * (lcm // divs1) + div2 * (lcm // divs2)
            # 用于约分的最大公因数
            _gcd = gcd(div, lcm)
            return f'{div // _gcd}/{lcm // _gcd}'

        return reduce(cal, findall('[+-]?\d+/\d+', expression))


ret = Solution()
print(ret.fractionAddition("-1/2+1/2"))
