def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [5, 4, 6, 8, 1, 0]
insert_sort(li)
