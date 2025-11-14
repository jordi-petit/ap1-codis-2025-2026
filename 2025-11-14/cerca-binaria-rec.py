"""
Cerca binaria recursiva
"""


def cerca(L: list[str], x: str) -> int | None:
    """
    Si x ∈ L, retorna una posició p tal que L[p] == x.
    Si x ∉ L, retorna None.
    Prec: L està en ordre creixent.
    Temps:  O(lg n), on n = |L|.
    """

    return cerca_rec(L, x, 0, len(L)-1)


def cerca_rec(L: list[str], x: str, esq: int, dre: int) -> int | None:
    """
    Si x ∈ L[esq..dre], retorna una posició p tal que L[p] == x.
    Si x ∉ L[esq..dre], retorna None.
    Prec: L està en ordre creixent.
    Temps:  O(lg n), on n = |L|.
    """

    if esq > dre:
        return None 
    mig = (esq + dre) // 2
    if L[mig] > x:
        return cerca_rec(L, x, esq, mig - 1)
    elif L[mig] < x:
        return cerca_rec(L, x, mig + 1, dre)
    else:  # L[mig] == x
        return mig
    