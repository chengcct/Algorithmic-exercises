"""计数排序,时间复杂度为O(n)"""
import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for idx, val in enumerate(count):
        for i in range(val):
            li.append(idx)


li = [random.randint(0, 100) for _ in range(1000)]
print(li)
count_sort(li)
print(li)
