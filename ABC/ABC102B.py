N = int(input())
A = list(map(int, input().split()))
M = 0
for i in range(N):
    for j in range(i + 1, N):
        if (max(A[i], A[j]) - min(A[i], A[j])) > M:
            M = (max(A[i], A[j]) - min(A[i], A[j]))
print(M)
