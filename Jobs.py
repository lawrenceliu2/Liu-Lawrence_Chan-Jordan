'''
Lawrence Liu and Jordan Chan
SoftDev1 pd8
HW#1 - Divine Your Destiny
2016-9-16
'''

#!/usr/bin/python

import random

def randjob():
    #store the data from the csv into a list, s
    a = open ('occupations.csv', 'r')
    s = a.read()
    s = s.split('\n')
    #remove the titles and blank data
    s = s[1:len(s)-2]

    #make a dictionary
    dict = {}
    for job in s:
        #the Occupation is the string job up to the last comma, the percent is whats after the last comma
        if (job[0] == '"'):
            dict[job[1:job.rfind('"')]] = float(job[job.rfind(',')+1:])
        else:
            dict[job[:job.rfind(',')]] = float(job[job.rfind(',')+1:])
    return weightedrand(dict)

def weightedrand(dict):
    r = random.random() * 99.8
    start = 0.0
    for job in dict:
        stop = start + dict[job]
        if (start <= r < stop):
            return job
        else:
            start = stop

print (randjob())
