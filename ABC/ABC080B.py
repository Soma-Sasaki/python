s = input()
a = int(s)
sum = 0
for i in s:
    sum += int(i)
if a / sum == int(a / sum):
    print('Yes')
else:
    print('No')
