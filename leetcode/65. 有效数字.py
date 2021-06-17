class Solution:
    def isNumber(self, s: str) -> bool:
        num_flag, e_flag, dot_flag = False, False, False
        # 准备0-9的数字
        nums = [str(i) for i in range(10)]

        for i, ch in enumerate(s):
            # 出现了数字
            if ch in nums:
                num_flag = True

            elif ch.lower() == 'e':
                if e_flag or not num_flag:
                    return False
                e_flag = True
                # e 后面要跟着数字
                num_flag = False

            elif ch == '.':
                # . 只能出现一次, 而且不能出现在e之后
                if dot_flag or e_flag:
                    return False

                dot_flag = True

            # 只能出现在开头或者在 e 后面
            elif ch == '+' or ch == '-':
                if i > 0 and s[i - 1].lower() != 'e':
                    return False

            # 其他字符
            else:
                return False
        # 返回是否出现数字
        return num_flag
