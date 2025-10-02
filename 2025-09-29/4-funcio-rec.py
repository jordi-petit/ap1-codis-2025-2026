def factorial(n: int) -> int:
    """
    Donat un natural n, retorna el seu factorial (n!).
    Prec: n >= 0.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
