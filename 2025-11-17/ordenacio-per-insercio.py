def insereix_ordenadament(L: list[float], i: int) -> None:
    """Insereix l'element i de L en L[:i], sabent que L[:i] està ordenat."""

    x = L[i]
    j = i - 1
    while j >= 0 and L[j] > x:
        L[j + 1] = L[j]
        j -= 1
    L[j + 1] = x


def ordena_per_insercio(L: list[float]) -> None:
    """Ordena la llista L en ordre creixent."""

    n = len(L)
    for i in range(1, n):
        insereix_ordenadament(L, i)
