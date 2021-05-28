def binary_search(li, var):
    left = 0
    right = len(li) - 1
    while left <= right:
        middle = (left + right) // 2
        if li[middle] == var:
            return middle
        elif li[middle] > var:
            right = middle - 1
        else:
            left = middle + 1
    return None


x = binary_search([1, 2, 3, 5, 6], 5)
print(x)
