import numpy as np

N, M = map(int, input().split())
tree =list(map(int, input().split()))
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    start = A[i][0]
    end = A[i][1]
    lack = M - int(np.average(tree[start-1:end]))
    if lack <= 0 :
        continue
    else:
        tree[start-1:end] = list(x+lack for x in tree[start-1:end])

print(*tree)
