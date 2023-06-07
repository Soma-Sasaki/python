n = int(input())
s = list(map(int, input().split()))
counter = -1
flag = False
while flag == False:
    counter += 1
    for a in range(n):
        if s[a] % 2 == 0:
            s[a] = s[a] / 2
        else:
            flag = True
print(counter)
