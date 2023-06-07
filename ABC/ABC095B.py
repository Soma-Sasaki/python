N, X = map(int, input().split())
m = list(int(input()) for i in range(N))
count = N
while X - sum(m) >= min(m):
    X = X - min(m)
    count += 1
print(count)
