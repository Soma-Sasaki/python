s, t = map(str, input().split())
st = s + t
ts = t + s
ST = []
TS = []
for i in range(len(st)):
    ST.append(ord(st[i])-96)
    TS.append(ord(ts[i])-96)

while len(ST)!=1:
    st = ST
    ts = TS
    ST = []
    TS = []
    for i in range(len(st)-1):
        tmp1 = st[i]+st[i+1]
        tmp2 = ts[i]+ts[i+1]
        if tmp1 > 101:
            tmp1 -= 101
        if tmp2 > 101:
            tmp2 -= 101
        ST.append(tmp1)
        TS.append(tmp2)

print(max(ST[0], TS[0]))
