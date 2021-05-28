def quick(list, left, right):
    """快速排序"""
    if left >= right:
        return
    middle = list[left]
    low = left
    high = right

    while low < high:
        # 左移
        while low < high and list[high] > middle:
            high -= 1
        list[low] = list[high]

        while low < high and list[low] < middle:
            low += 1
        list[high] = list[low]
        # 退出时low==high
    list[low] = middle

    quick(list, left, low - 1)
    quick(list, low + 1, right)


if __name__ == '__main__':
    li = [9, 56, 4, 3, 45, 455, 44]
    print(li)
    quick(li, 0, len(li) - 1)
    print(li)
