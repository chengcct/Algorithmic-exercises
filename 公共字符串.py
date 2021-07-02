def get_string(str1, str2):
    min_len = len(str1) if len(str1) < len(str2) else len(str2)
    example = str1 if len(str1) < len(str2) else str2
    other = str2 if str1 == example else str1
    for i in range(min_len):
        for j in range(min_len, 0, -1):
            if other.find(example[i:j]) != -1:
                return example[i:j]


print(get_string('loe', 'loved'))
