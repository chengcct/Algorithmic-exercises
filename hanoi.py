"""汉诺塔"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('moving from %s to %s' % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, 'A', 'B', 'C')


# def linear_search(li, val):
#     for idx, v in enumerate(li):
#         if v == val:
#             return idx
#     else:
#         return None
#
#
# x = linear_search([1, 3, 5, 4, 6], 5)
# print(x)
