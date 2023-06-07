A, B, K = map(int, input().split())
arr = range(A, B + 1)
ans = []
for i in range(K):
    ans.append(A + i)
for j in range(K):
    ans.append(B + 1 - K + j)

anset = list(set(ans))
anset.sort()
if A + K <= B + 1:
    for ele in range(len(anset)):
        print(anset[ele])
else:
    for ele in range(A, B + 1):
        print(ele)
        
