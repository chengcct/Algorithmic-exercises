def merge(list):
    """归并排序"""
    n = len(list)
    if n <= 1:
        return list
    mid = n // 2

    left_li = merge(list[:mid])
    right_li = merge(list[mid:])

    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_li) and right_point < len(right_li):
        if left_li[left_point] < right_li[right_point]:
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1

    result += left_li[left_point:]
    result += right_li[right_point:]
    return result


if __name__ == '__main__':
    li = [9, 56, 4, 3]
    print(li)
    sort = merge(li)
    print(sort)
