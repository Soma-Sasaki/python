A = []
A.append(1)
A.append(1)

i = 0
j = 0

n = int(input())

while True:
    if A[i] + A[i + 1] > n:
        break
    A.append(A[i] + A[i + 1])
    i += 1

print(A)

for j in range(0, i + 2):
    print(A[j])
