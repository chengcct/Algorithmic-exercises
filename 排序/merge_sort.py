"""归并排序"""
import random


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    temp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1
    while i <= mid:
        temp.append(li[i])
        i += 1
    while j <= high:
        temp.append(li[j])
        j += 1
    li[low:high + 1] = temp


def sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        sort(li, low, mid)
        sort(li, mid + 1, high)
        merge(li, low, mid, high)


li = list(range(16))
random.shuffle(li)
print(li)
sort(li, 0, len(li) - 1)
print(li)
