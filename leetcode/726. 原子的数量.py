class Solution:
    def countOfAtoms(self, f: str) -> str:
        i = 0
        n = len(f)
        element_info = list()  # list of [element_name, number_of_element, number_of_parentheses]
        parentheses_stack = list()
        # atom = str()
        distribution = dict()
        while i < n:
            # 如果遇到的是字母
            # 如果遇到的是大写字母
            atom = str()
            if f[i].isupper():
                atom = f[i]
                i += 1
            # 跟着小写字母
            while i < n and f[i].islower():
                atom += f[i]
                i += 1
            cnt = str()
            # 如果后面有数
            if i < n and f[i].isdigit():
                # 遍历所有的数
                while i < n and f[i].isdigit():
                    cnt += f[i]
                    i += 1
                element_info.append([atom, int(cnt), len(parentheses_stack)])
            # 如果后面没有数
            else:
                # 如果前面的if都执行过（即得到了某一个atom，而不是一开始就从(开头）
                # print("i, atom:", i, atom)
                if len(atom) and len(cnt) == 0:
                    element_info.append([atom, 1, len(parentheses_stack)])
                if i < n and f[i] == '(':
                    parentheses_stack.append('(')
                    i += 1
                elif i < n and f[i] == ')':
                    i += 1
                    cnt = str()
                    if i < n and f[i].isdigit():
                        # 遍历所有的数
                        while i < n and f[i].isdigit():
                            cnt += f[i]
                            i += 1
                        cnt = int(cnt)
                    else:
                        cnt = 1
                    # parentheses_stack.pop()
                    for k in range(len(element_info) - 1, -1, -1):
                        if element_info[k][2] == len(parentheses_stack):
                            element_info[k][1] *= cnt
                            element_info[k][2] -= 1
                        else:
                            break
                    parentheses_stack.pop()

        # print(element_info)
        for ele in element_info:
            if ele[0] in distribution:
                distribution[ele[0]] += ele[1]
            else:
                distribution[ele[0]] = ele[1]

        # print(distribution)
        lst = sorted(distribution.items(), key=lambda obj: obj[0])
        # print(lst)
        ans = str()
        for name, number in lst:
            if number == 1:
                ans += name
            else:
                ans += name + str(number)
        return ans
