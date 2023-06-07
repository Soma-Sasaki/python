N, X = map(int, input().split())
XX = bin(X)
for _ in range(N):
    a = int(input())
    print(XX[-a])
