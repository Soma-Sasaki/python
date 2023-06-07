
s = int(input())
a = 0
if s % 10 == 1:
    a += 1
if int(s / 10) % 10 == 1:
    a += 1
if int(s / 100) % 10 == 1:
    a += 1

print(a)
