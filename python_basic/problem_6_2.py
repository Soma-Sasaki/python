def avg_nums(nums):
    s=0
    for i in nums:
        print(i)
        s += i
    return s / len(nums)


def max_nums(nums):
    for i, n in enumerate(nums):
        if i == 0:
            max_num = n
        if max_num < n:
            max_num = n
    return max_num


def min_nums(nums):
    for i, n in enumerate(nums):
        if i == 0:
            min_num = n
        if min_num > n:
            min_num = n
    return min_num

a=[]
while True:
    S=input("数値を入力:")
    if S !="":
        a.append(int(S))
    else:
        break

print("平均値は{}, 最大値は{},最小値は{}です".format(avg_nums(a),max_nums(a),min_nums(a)))
