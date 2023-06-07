D, N = map(int, input().split())
ans = 100**D
for i in range(N - 1):
    ans += 100**D
    if ans % 100**(D + 1)==0:
        ans += 100**D
print(ans)
