"""Croba i floc de Koch"""

import turtle
import yogi


def corba_koch(m: float, n: int) -> None:
    if n == 0:
        turtle.forward(m)
    else:
        corba_koch(m / 3, n - 1)
        turtle.left(60)
        corba_koch(m / 3, n - 1)
        turtle.right(120)
        corba_koch(m / 3, n - 1)
        turtle.left(60)
        corba_koch(m / 3, n - 1)


def floc_koch(m: float, n: int) -> None:
    for _ in range(3):
        corba_koch(m, n)
        turtle.right(120)


def main() -> None:
    m = yogi.read(float)
    n = yogi.read(int)
    floc_koch(m, n)
    turtle.done()


if __name__ == "__main__":
    main()
