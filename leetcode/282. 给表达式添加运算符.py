from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def calculate(num, target, expression, prev, ans, results):
            if len(num) == 0 and ans == target:
                results.append(expression)
            else:
                for i in range(1, len(num) + 1):
                    if i > 1 and num[0] == '0':
                        continue
                    a = int(num[0:i])
                    if expression == '':
                        calculate(num[i:len(num)], target, num[0:i], a, a, results)
                    else:
                        calculate(num[i:len(num)], target, expression + '+' + num[0:i], a, ans + a, results)
                        calculate(num[i:len(num)], target, expression + '-' + num[0:i], -a, ans - a, results)
                        calculate(num[i:len(num)], target, expression + '*' + num[0:i], a * prev, ans + prev * (a - 1), results)

        results = []
        calculate(num, target, '', 0, 0, results)
        return results


ret = Solution()
print(ret.addOperators("123", 6))
