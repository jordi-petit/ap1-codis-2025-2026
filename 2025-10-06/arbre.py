"""Arbres fractals"""

import turtle
import yogi


def arbre(m: float, n: int) -> None:
    """..."""
    if n == 0:
        turtle.forward(m)
        turtle.backward(m)
    else:
        turtle.forward(m / 2)
        turtle.right(45)
        arbre(m / 2, n - 1)
        turtle.left(90)
        arbre(m / 2, n - 1)
        turtle.right(45)
        turtle.backward(m / 2)


def main() -> None:
    m = yogi.read(float)
    n = yogi.read(int)
    turtle.left(90)
    arbre(m, n)
    turtle.done()


if __name__ == "__main__":
    main()
