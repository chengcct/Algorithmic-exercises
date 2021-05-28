import random


def shell(li, gap):
    for i in range(gap, len(li)):
        temp = li[i]
        j = i - gap
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = temp


def sort(li):
    d = len(li) // 2
    while d >= 1:
        shell(li, d)
        d //= 2


li = list(range(20))
random.shuffle(li)
print(li)
sort(li)
print(li)
