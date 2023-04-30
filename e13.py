#usr/bin/env python
#-*-coding:utf-8-*-
from test import testEqual

def somaAte(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma
t = somaAte(0)
testEqual(t, 0)
testEqual(somaAte(10), 55)
testEqual(somaAte(1),1)
exit(0)
