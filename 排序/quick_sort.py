def quick_sort(list, left, right):
    if left >= right:
        return
    mid = list[left]
    low = left
    high = right

    while low < high:
        while low < high and list[high] > mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < mid:
            low += 1
        list[high] = list[low]
    list[low] = mid

    quick_sort(list, left, low - 1)
    quick_sort(list, low + 1, right)


if __name__ == '__main__':
    li = [9, 56, 4, 3, 45, 455, 44]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
