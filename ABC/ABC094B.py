N, M, X = map(int, input().split())
A = list(map(int, input().split()))
goalA = 0
goalB = 0
for i in range(1, X):
    goalA += A.count(i)
for j in range(X + 1, N):
    goalB += A.count(j)
print(min(goalA, goalB))
