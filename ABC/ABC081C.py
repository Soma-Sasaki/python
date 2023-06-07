N, K = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * (N + 1)
for i in range(N):
    C[A[i]] += 1
A_sort = sorted(C, reverse=True)

print(sum(A_sort[K:]))
