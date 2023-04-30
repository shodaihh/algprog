#usr/bin/env python3
#-*-coding:utf-8-*-
from test import testEqual

def somaAte(n):
    return n * (n + 1) // 2
t = somaAte(0)
testEqual(t, 0)
t = somaAte(10)
testEqual(t, 55)
t = somaAte(1)
testEqual(t,1)
exit(0)
