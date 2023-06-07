import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

def pleaseConform(caps):
    intervals = []
    start = forward = backward = 0
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            ForB = caps[start]
            intervals.append((start, i-1, ForB))
            if ForB == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    ForB = caps[start]
    intervals.append((start, len(caps)-1, ForB))
    if ForB == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] != t[1]:
                print("People in positions {} through {} flip your caps! \n".format(t[0], t[1]))
            else:
                print("Person in position {} flip your cap! \n".format(t[0]))

pleaseConform(cap1)
pleaseConform(cap2)
pleaseConform([])
