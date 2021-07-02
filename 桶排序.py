def bucket_sort(nums):
    max_num = max(nums)
    bucket = [0] * (max_num + 1)
    for i in nums:
        bucket[i] += 1
    sort_nums = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for x in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


nums = [5, 6, 8, 7, 4, 11, 4]
print(bucket_sort(nums))
