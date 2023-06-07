zsum = 0
for s in open("leavetime.txt"):
    h = int(s[0:2])
    m = int(s[3:5])
    zangyo = h * 60 + m - 1040
    if zangyo > 0:
        zsum += zangyo
a = int(zsum / 60)
b = zsum % 60
print("今月の総残業時間は{0}時間{1}分です".format(a,b))
