def escriure_hola(cops: int) -> None:
    """Escriu "hola" cops vegades."""

    # implementació recursiva
    if cops == 0:       # millor: if cops > 0: ... i sense else
        pass
    else:
        escriure_hola(cops - 1)
        print("hola")


escriure_hola(4)
