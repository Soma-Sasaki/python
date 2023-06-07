def bestTimetoPartySmart(schedule, ystart, yend):
    sortList1(schedule)
    times = []
    for s in schedule:
        if (s[0] >= yend) or (s[1] <= ystart):
            continue
        times.append((s[0], "start", s[2]))
        times.append((s[1], "end", s[2]))
    sortList2(times)
    max_count, time = chooseTime(times)
    if max_count == 0:
        print("Sorry, but you can't meet anyone.")
    else:
        print("Best time to attend the party is at {} o\'clock : {} celebrities will be attending!".format(time, max_count))

def sortList1(slist):
    for i1 in range(len(slist)-1):
        i2 = i1
        for i in range(i1+1, len(slist)):
            if slist[i][0] < slist[i2][0]:
                i2 = i
        slist[i1], slist[i2] = slist[i2], slist[i1]

def sortList2(tlist):
    for i1 in range(len(tlist)-1):
        i2 = i1
        for i in range(i1+1, len(tlist)):
            if tlist[i][0] < tlist[i2][0]:
                i2 = i
        tlist[i1], tlist[i2] = tlist[i2], tlist[i1]

def chooseTime(times):
    rcount = 0
    max_count, time = 0, 0
    for t in times:
        if t[1] == "start":
            rcount += t[2]
        elif t[1] == "end":
            rcount -= t[2]
        if (rcount > max_count):
            max_count = rcount
            time = t[0]
    return max_count, time

bestTimetoPartySmart([(6.0, 8.0, 2), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (8.0, 9.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7), (6.5, 12.0, 1)], 4, 6.5)
