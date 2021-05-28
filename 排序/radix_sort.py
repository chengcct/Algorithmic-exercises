"""基数排序"""
import random


def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # it=1 988//10->98 98%10->8; it=2 988//100->9 9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写回li
        it += 1


li = list(range(10000))
random.shuffle(li)
radix_sort(li)
print(li)
