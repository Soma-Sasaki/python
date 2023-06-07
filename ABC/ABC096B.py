A, B, C = map(int, input().split())
K = int(input())
m = max(A, B, C)
for i in range(K):
    m = 2 * m
print(A + B + C - max(A, B, C) + m)
