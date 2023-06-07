N = int(input())
D, X = map(int, input().split())
A = list(int(input()) for i in range(N))
sum = 0
for i in range(N):
    B = 0
    while B * A[i] + 1 <= D:
        B += 1
        sum += 1
print(X + sum)
