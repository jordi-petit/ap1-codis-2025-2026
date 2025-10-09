"""Comptar quants 'gat' hio ha en seqüència de paraules."""

from yogi import tokens


gats = 0
for paraula in tokens(str):
    if paraula == "gat":
        gats = gats + 1
print(gats)
