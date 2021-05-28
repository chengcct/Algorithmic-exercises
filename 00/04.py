def select(list):
    """选择排序"""
    l = len(list)
    for j in range(l-1):
        min_index = j
        for i in range(j+1, l):
            if list[min_index] > list[i]:
                min_index = i
        list[j], list[min_index] = list[min_index], list[j]


if __name__ == '__main__':
    li = [9, 56, 4, 3, 45, 455, 44]
    print(li)
    select(li)
    print(li)
