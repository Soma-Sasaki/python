import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'B', 'B']

def pleaseConform(caps):
    if len(caps) == 0:
        return caps
    intervals = []
    tmp = 0
    caps += [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] == 'H':
            if tmp != 0:
                print("Person at position {} flip your cap! \n".format(tmp))
            tmp = 0
            continue
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                tmp = i
            elif tmp != 0:
                if tmp != i-1:
                    print("People in positions {} through {} flip your caps! \n".format(tmp, i-1))
                    tmp = 0
                else:
                    print("Person at position {} flip your cap! \n".format(tmp))
                    tmp = 0

pleaseConform(cap1)

pleaseConform(cap2)

pleaseConform(cap3)
