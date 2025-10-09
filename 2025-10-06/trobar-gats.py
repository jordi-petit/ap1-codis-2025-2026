"""Trobar si una seqüència de paraules conté algun 'gat'."""

from yogi import scan


hi_ha_gats = False
paraula = scan(str)
while paraula != None and not hi_ha_gats:
    if paraula == "gat":
        hi_ha_gats = True
    else:
        paraula = scan(str)

if hi_ha_gats:
    print("Hi ha gats")
else:
    print("no hi ha gats")
