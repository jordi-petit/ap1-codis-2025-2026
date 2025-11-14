import random
import time


def posicio_minim(L: list[float], i: int) -> int:
    """Retorna la posició de l'element més petit de L[i:] amb 0 ≤ i < len(L)."""

    n = len(L)
    m = i
    for j in range(i + 1, n):
        if L[j] < L[m]:
            m = j 
    return m


def ordena_per_seleccio(L: list[float]) -> None:
    """Ordena la llista L en ordre creixent."""

    n = len(L)
    for i in range(n-1):
        m = posicio_minim(L, i)
        L[i], L[m] = L[m], L[i]



def main():
    for n in range(1000, 15001, 1000):
        llista = [random.random() for _ in range(n)]
        t1 = time.perf_counter()
        ordena_per_seleccio(llista)
        t2 = time.perf_counter()
        print(n, t2 - t1)


if __name__ == "__main__":
    main()
