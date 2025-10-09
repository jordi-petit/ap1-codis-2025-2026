"""Calcular la mitjana d'una seqüència no buida de reals."""

from yogi import tokens

s = 0.0
n = 0
for x in tokens(float):
    s = s + x
    n = n + 1
print(s / n)
