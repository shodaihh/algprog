#usr/bin/env python3
#-*-coding:utf-8-*-
from test import testEqual
import math

def areaDeCirculo(r):
    return math.pi * r**2

t = areaDeCirculo(0)
testEqual(t,0)
t = areaDeCirculo(1)
testEqual(t,math.pi)
t = areaDeCirculo(100)
testEqual(t,31415.926535897932)
exit(0)
