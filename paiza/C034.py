s=list(input().split())
ans=0
if s[0]=="x":
    if s[1]=="+":
        ans=int(s[4])-int(s[2])
    else:
        ans=int(s[4])+int(s[2])
elif s[2]=="x":
    if s[1]=="+":
        ans=int(s[4])-int(s[0])
    else:
        ans=int(s[0])-int(s[4])
else:
    if s[1]=="+":
        ans=int(s[0])+int(s[2])
    else:
        ans=int(s[0])-int(s[2])


print(ans)
