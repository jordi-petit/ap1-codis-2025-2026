from turtle import done, right, forward


def pintar_quadrat(mida: int) -> None:
    """Pinta un quadrat de la mida donada."""

    for _ in range(4):
        forward(mida)
        right(90)


def pintar_quadrats_girats(mida: int, quants: int) -> None:
    """..."""

    for _ in range(quants):
        pintar_quadrat(mida)
        right(360 / quants)


pintar_quadrats_girats(100, 5)
done()
