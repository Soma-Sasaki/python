N, M = map(int, input().split())
p = 0
for i in range(M):
    f = int(input())
    if p >= f:
        p -= f
    else:
        N -= f
        p += f * 0.1
    print(N, int(p))
