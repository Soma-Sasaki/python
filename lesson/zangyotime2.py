gd = {}
TG=17*60+20
for s in open("leavetime2.txt"):
    A = s[:-1].split(" ")
    name = A[0]
    time = A[1].split(":")
    hour = int(time[0])
    minute = int(time[1])
    zangyo = hour * 60 + minute - TG
    if zangyo < 0:
        zangyo += 24 * 60
    gd.setdefault(name, 0)
    gd[name] = gd[name] + zangyo

for i in gd:
    print("{0}の残業時間は{1}時間{2}分です".format(i,gd[i]/60,gd[i]%60))
