n = int(input())
a = list(int(input()) for _ in range(n))
a.sort()
for i in range(n):
    print(a[i])
