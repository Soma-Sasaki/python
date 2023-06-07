def bestTimetoParty(schedule):
    start = min([s[0] for s in schedule])
    end = max([s[1] for s in schedule])
    count = celebrityDensity(schedule, start, end)
    max_count = max(count)
    time = count.index(max_count) + start
    print("Best time to attend the party is at {} o\'clock : {} celebrities will be attending!".format(time, max_count))

def celebrityDensity(sch, s, e):
    count = []
    for i in range(s, e):
        tmp = 0
        for c in sch:
            if c[0] <= i and i < c[1]:
                tmp += 1
        count.append(tmp)
    return count

bestTimetoParty([(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)])
