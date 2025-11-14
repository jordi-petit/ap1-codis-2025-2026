"""
Cerca binaria iterativa
"""

def cerca_binaria_ite(L: list[str], x: str) -> int | None:
    """
    Si x ∈ L, retorna una posició p tal que L[p] == x.
    Si x ∉ L, retorna None.
    Prec: L està en ordre creixent.
    Temps: O(lg n), on n = |L|.
    """

    esq, dre = 0, len(L) - 1
    while esq <= dre:
        mig = (esq + dre) // 2
        if L[mig] > x:
            dre = mig - 1
        elif L[mig] < x:
            esq = mig + 1
        else:
            return mig 
    return None

