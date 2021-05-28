def insert(list):
    """插入排序"""
    l = len(list)
    for j in range(1, l):
        i = j
        while i > 0:
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [9, 56, 4, 3, 45, 455, 44]
    print(li)
    insert(li)
    print(li)
