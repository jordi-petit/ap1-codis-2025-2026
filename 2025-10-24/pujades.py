# https://jutge.org/problems/P62060

from yogi import tokens


def pujada() -> int:
    """Llegeix l'entrada i calcula la longitud màxima d'una pujada."""

    max_pujada = 0  # longitud de la pujada més gran trobada fins ara
    ultim = None  # últim element llegit
    ultima_pujada = 0  # longitud de la pujada més gran que acaba en l'últim element llegit fins ara

    for x in tokens(int):
        if ultim is None or x > ultim:
            ultima_pujada += 1
            if ultima_pujada > max_pujada:
                max_pujada = ultima_pujada
        else:
            ultima_pujada = 1
        ultim = x

    return max_pujada


def main() -> None:
    print(pujada())


if __name__ == "__main__":
    main()
