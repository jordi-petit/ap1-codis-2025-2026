def fusio(L1: list[float], L2: list[float]) -> list[float]:
    """
    Prec: L1 està en ordre creixent i L2 està en ordre creixent.
    Retorna la fusió de L1 i L2 en ordre creixent.
    """

    R = list[float]()
    i1, i2 = 0, 0 
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] <= L2[i2]:
            R.append(L1[i1])
            i1 += 1
        else:
            R.append(L2[i2])
            i2 += 1
    R.extend(L1[i1:])
    R.extend(L2[i2:])
    return R


