"""Trobar si una seqüència de paraules conté algun 'gat'."""

from yogi import tokens


def hi_ha_gats() -> bool:
    for paraula in tokens(str):
        if paraula == "gat":
            return True
    return False


if hi_ha_gats():
    print("Hi ha gats")
else:
    print("no hi ha gats")
