import yogi


def bona(paraula: str, objectiu: str) -> bool:
    """..."""
    if len(paraula) < 3:
        return False
    if objectiu[0] not in paraula:
        return False
    for lletra in paraula:
        if lletra not in objectiu:
            return False
    return True


def tuti(paraula: str, objectiu: str) -> bool:
    """..."""
    for lletra in objectiu:
        if lletra not in paraula:
            return False
    return True


def punts(paraula: str, objectiu: str) -> int:
    if len(paraula) <= 3:
        return 1
    elif len(paraula) <= 4:
        return 2
    elif tuti(paraula, objectiu):
        return len(paraula) + 10
    else:
        return len(paraula)


def puntuacio(paraules: list[str], objectiu: str) -> int:
    return sum([punts(paraula, objectiu) for paraula in paraules])


def cercar_paraules(objectiu: str) -> list[str]:
    """..."""
    trobades = list[str]()
    for paraula in yogi.tokens(str):
        if bona(paraula, objectiu):
            trobades.append(paraula)
    return trobades


def main() -> None:
    objectiu = yogi.read(str)
    trobades = cercar_paraules(objectiu)
    for trobada in sorted(trobades):
        print(trobada)
    print("-----")
    print(puntuacio(trobades, objectiu))


if __name__ == "__main__":
    main()
