"""Trobar el màxim en una seqüència no buida de reals."""

from yogi import read, tokens

m = read(float)
for x in tokens(float):
    if x > m:
        m = x
print(m)
