"""
Cerca lineal
"""


def cerca(L: list[str], x: str) -> int | None:
    """
    Si x ∈ L, retorna una posició p tal que L[p] == x.
    Si x ∉ L, retorna None.
    Temps: O(n), on n = |L|
    """

    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
