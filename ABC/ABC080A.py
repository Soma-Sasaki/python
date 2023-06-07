n, a, b = map(int, input().split())
min = 0
if b >= a * n:
    min = a * n
else:

    min = b

print(min)
