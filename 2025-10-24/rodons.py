# https://jutge.org/problems/X87201

from yogi import tokens, read


def is_round(n: int, b: int) -> bool:
    """Determina si n es redondo en base b"""

    num_digits, sum_digits = 0, 0
    while n > 0:
        num_digits += 1
        sum_digits += n % b
        n //= b
    return num_digits == sum_digits


def bi_round() -> bool:
    """Lee la entrada y devuelve un booleano indicando si la secuencia es bi-redonda.
    Deja de procesar la entrada en cuanto encuentra dos pares redondos"""
    rounds = 0
    for x in tokens(int):
        b = read(int)
        if is_round(x, b):
            rounds += 1
            if rounds == 2:
                return True
    return False


def main() -> None:
    if bi_round():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
