N = int(input())
s = list(input() for i in range(N))
M = int(input())
t = list(input() for i in range(M))

s_set = list(set(s))
ans = 0
for name in s_set:
    count = s.count(name) - t.count(name)
    ans = max(count, ans)

print(ans)
