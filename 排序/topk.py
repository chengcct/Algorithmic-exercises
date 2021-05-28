import random


def sift(li, low, high):
    """
    topk，排序出最大的数
    :param li: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = i * 2 + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 建堆
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 遍历
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    # 出数
    return heap


li = list(range(1000))
random.shuffle(li)
print(topk(li, 10))
