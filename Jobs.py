#!/usr/bin/python

import random

def randjob():
    a = open ('occupations.csv', 'r')
    s = a.read()
    s = s.split('\r\n')
    return s

print randjob()
