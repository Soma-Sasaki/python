s=input()
t=input()

ss=''.join(sorted(s))#辞書順最小=辞書で一番最初
tt=''.join(sorted(t,reverse=True))#辞書順最大

if ss<tt:
    print('Yes')
else:
    print('No')
