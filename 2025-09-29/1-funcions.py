def maxim2(a: int, b: int) -> int:
    """Donats dos enters, retorna el més gran."""

    if a > b:
        return a
    else:
        return b


def maxim3(a: int, b: int, c: int) -> int:
    """Donats tres enters, retorna el més gran."""

    return maxim2(a, maxim2(b, c))


def valor_absolut(a: float) -> float:
    """
    Donat un real, retorna el seu valor absolut.
    """

    if a >= 0:
        return a
    else:
        return -a


def factorial(n: int) -> int:
    """
    Donat un natural n, retorna el seu factorial (n!).
    Prec: n >= 0.
    """

    f = 1
    while n >= 1:
        f = f * n
        n = n - 1
    return f


def minim_i_maxim(a: int, b: int) -> tuple[int, int]:
    if a > b:
        return b, a
    else:
        return a, b


def suma_1_segon(h: int, m: int, s: int) -> tuple[int, int, int]:
    """..."""
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return h, m, s


def es_primer(n: int) -> bool:
    """
    Donat un nombre n, diu si és primer.
    Prec: n >= 0.
    """

    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        print(d)
        if n % d == 0:
            return False
        d = d + 1
    return True


print(es_primer(21))
