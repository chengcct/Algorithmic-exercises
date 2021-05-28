def bubble(list):
    """冒泡排序"""
    l = len(list)
    for j in range(l - 1):
        count = 0
        for i in range(l - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        if 0 == count:
            return


if __name__ == '__main__':
    a = [1, 3, -5, 4, 78, 35, 6545, 654]
    b = [1, 5, 4, 7, 8, 9]
    print(b)
    bubble(b)
    print(b)
