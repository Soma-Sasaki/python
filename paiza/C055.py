N=int(input())
G=input()
a=0
for _ in range(N):
    S=input()
    if G in S:
        print(S)
        a+=1

if a==0:
    print("None")
