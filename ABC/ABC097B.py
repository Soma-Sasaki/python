X = int(input())
m = 1
for i in range(1, 33):
    for j in range(2, 11):
        if i**j <= X and i**j > m:
            m = i**j
print(m)
