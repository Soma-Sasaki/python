def max_nums(a):
    for i, n in enumerate(a):
        if i == 0:
            max = n
        if n > max:
            max = n
    return max


def sort_nums(*a):
    list_nums = list(a)
    result = []
    while len(list_nums) > 0:
        value=max_nums(list_nums)
        result.append(value)
        list_nums.remove(value)
    return tuple(result)


result = sort_nums(1, 5, 2, -2, 4, 7)
print(result)
