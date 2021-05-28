import random


def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return li


# li = [random.randint(0, 10000) for i in range(10000)]
li = [9, 6, 5, 8, 7, 1, 2, 3]
print(li)
bubble_sort(li)
