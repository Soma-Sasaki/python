N=int(input())

ans=0

for _ in range(N):

    meibo=list(input().split())
    score=list(map(int,meibo[1:]))

    if meibo[0]=="s" and sum(score)>=350 and sum(score[1:3])>=160:
        ans+=1
    if meibo[0]=="l" and sum(score)>=350 and sum(score[3:5])>=160:
        ans+=1

print(ans)
