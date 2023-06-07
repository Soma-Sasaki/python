import math

print("数字を入力してください")
n = int(input())

A = list(range(2, n + 1))

i = 0

while True:
    p = A[i]
    if p > math.sqrt(n):
        break
    print("{0}の倍数をふるい落とす".format(p))
    for j in A[i + 1:]:
        if j % p == 0:
            A.remove(j)
    print(A)
    i += 1

print("{0}までの素数 計{1}個".format(n, len(A)))
print(A)
