a,b=map(int,input().split())
S=input()
if len(S) == a + b + 1 and S[a] == '-' and S.count('-') == 1:
    print('Yes')
else:
    print('No')
