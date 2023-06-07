Q = int(input())
for _ in range(Q):
    N = int(input())
    s = 0
    for i in range(1, N):
        if N % i == 0:
            s += i
    if N==s:
        print("perfect")
    elif abs(N-s)==1:
        print("nearly")
    else:
        print("neither")
