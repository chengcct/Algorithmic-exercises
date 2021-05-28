def select_sort(li):
    for i in range(len(li) - 1):
        min = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min]:
                min = j
        li[i], li[min] = li[min], li[i]
        print(li)


li = [9, 2, 3, 5, 6, 4, 1]
print(li)
select_sort(li)
