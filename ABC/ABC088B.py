N = int(input())
a = list(map(int, input().split()))
asort = sorted(a, reverse=True)
#a.sort(reverse=True)
A = 0
B = 0
for i in range(N):
    if i % 2 == 0:
        A += asort[i]
    else:
        B += asort[i]

print(A - B)
