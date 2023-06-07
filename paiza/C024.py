n = int(input())
a, b = 0, 0

for _ in range(n):
    s=list(input().split())
    if s[0]=="SET":
        if s[1]=="1":
            a=int(s[2])
        else:
            b=int(s[2])
    elif s[0]=="ADD":
        b=a+int(s[1])
    else:
        b=a-int(s[1])

print(a,b)
