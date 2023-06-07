A, B = map(int, input().split())
L = list(range(A, B + 1))
count = 0

for i in L:
    tmp = list(str(i))
    if tmp[0] == tmp[4] and tmp[1] == tmp[3]:
        count += 1

print(count)
