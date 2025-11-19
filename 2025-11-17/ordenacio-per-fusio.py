def ordena_per_fusio(L: list[float]) -> None:
    ordena_per_fusio_rec(L, 0, len(L) - 1)


def ordena_per_fusio_rec(L: list[float], e: int, d: int) -> None:
    if e < d:
        m = (e + d) // 2
        ordena_per_fusio_rec(L, e, m)
        ordena_per_fusio_rec(L, m + 1, d)
        fusio(L, e, m, d)


def fusio(L: list[float], e: int, m: int, d: int) -> None:
    """
    L[e..m] està ordenada
    L[m+1..d] està ordenada
    => L[e..d] ordenada
    """

    A = list[float]()
    i1, i2 = e, m + 1
    while i1 <= m and i2 <= d:
        if L[i1] <= L[i2]:
            A.append(L[i1])
            i1 += 1
        else:
            A.append(L[i2])
            i2 += 1
    if i2 <= d:
        L[e:i2] = A
    else:
        A.extend(L[i1:m+1])
        L[e:d+1] = A
        

