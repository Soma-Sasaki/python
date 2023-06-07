N=int(input())
d=[]
for i in range(N):
    d.append(int(input()))　#縦に並べて値が与えられたとき
print(len(set(d)))
#print(len(set(int(input()) for i in range(n))))
