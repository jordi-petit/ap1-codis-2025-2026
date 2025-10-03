"""
Programa que compta quants nombres primers
hi ha a la seqüència d'entrada.
"""

from yogi import tokens


def es_primer(n: int) -> bool:
    """
    Donat un nombre n, diu si és primer.
    Prec: n >= 0.
    """

    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


def main() -> None:
    c = 0  # comptador de nombres primers
    for x in tokens(int):
        if es_primer(x):
            c = c + 1
    print(c)


if __name__ == "__main__":
    main()

# aquesta és la *bona* manera de tenir el programa principal
