A,B=input().split()
n=max(len(A),len(B))
ans=0
for i in range(n):
    ans[i]=int(A[i])+int(B[i])
    if len(ans[i])==1:
        print(ans,end="")
    else:
        print(ans%10,end="")
