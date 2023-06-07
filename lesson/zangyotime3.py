gd = {}
TG = 17 * 60 + 20

for s in open("leavetime3.txt"):
    A = s[:-1].split(",")
    k = A[0][:6] + "," + A[1]
    time = A[2].split(":")
    hour = int(time[0])
    minute = int(time[1])
    zangyo = hour * 60 + minute - TG
    if zangyo < 0:
        zangyo += 24 * 60
    gd.setdefault(k, 0)
    gd[k] = gd[k] + zangyo

saicho=0
for i in gd:
    if saicho<gd[i]:
        longest_person=[i]
        saicho=gd[i]
    elif saicho==gd[i]:
        longest_person.append(i)

print("残業時間最多は{0}で、{1}時間{2}分です".format(longest_person,int(saicho/60),saicho%60))
