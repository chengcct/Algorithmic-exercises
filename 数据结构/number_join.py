from functools import cmp_to_key

li = [32, 45, 89, 4, 223, 23333]


def xy_cmp(x, y):
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return ''.join(li)


print(number_join(li))
