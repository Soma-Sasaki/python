N = int(input())
S = input()
count = 0
for i in range(1, N):
    count = max(count, len(set(S[:i]) & set(S[i:])))
print(count)
