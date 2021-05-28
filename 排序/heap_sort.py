import random


def sift(li, low, high):
    """
    堆排序
    :param li: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = i * 2 + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:  # 右孩子较大
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 建堆完成
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high


li = [i for i in range(100)]

random.shuffle(li)
print(li)
heap_sort(li)
print(li)
