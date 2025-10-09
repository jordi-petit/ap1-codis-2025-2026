"""Comptar nombre de paraules consecutives repetides."""

from yogi import tokens, scan

r = 0
p1 = scan(str)
if p1 != None:
    for p2 in tokens(str):
        if p1 == p2:
            r = r + 1
        p1 = p2
print(r)
