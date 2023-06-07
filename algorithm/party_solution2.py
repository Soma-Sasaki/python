def bestTimetoPartySmart(schedule, ystart, yend):
    sortList(schedule)
    times = []
    for s in schedule:
        if (s[0] >= yend) or (s[1] <= ystart):
            continue
        times.append(s)
    print(times)
    max_count, time = chooseTime(times)
    if max_count == 0:
        print("Sorry, but you can't meet anyone.")
    else:
        print("Best time to attend the party is at {} o\'clock : {} celebrities will be attending!".format(time, max_count))

def sortList(slist):
    for i1 in range(len(slist)-1):
        i2 = i1
        for i in range(i1+1, len(slist)):
            if slist[i][0] < slist[i2][0]:
                i2 = i
        slist[i1], slist[i2] = slist[i2], slist[i1]

def chooseTime(times):
    rcount = 0
    max_count, time = 0, 0
    for t1 in times:
        for t2 in times:
            if (t2[0] <= t1[0]) and (t2[1] > t1[0]):
                rcount += 1
        if (rcount > max_count):
            max_count = rcount
            time = t1[0]
        rcount = 0
    return max_count, time

bestTimetoPartySmart([(6.5, 12.0), (6.5, 7.0), (7.5, 10.0), (8.0, 10.0), (6.0, 8.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (8.0, 9.0), (11.0, 12.0), (7.0, 8.0)], 3.0, 7)
