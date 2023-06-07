E = input().split("+")

count1 = 0
count10 = 0
sum = 0

for i in range(len(E)):
    count1 = E[i].count("/")
    count10 = E[i].count("<")
    sum += 10*count10 + count1

print(sum)
