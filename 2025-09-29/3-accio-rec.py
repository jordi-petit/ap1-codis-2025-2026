def escriure_hola(cops: int) -> None:
    """Escriu "hola" cops vegades."""

    if cops == 0:
        pass
    else:
        print("hola")
        escriure_hola(cops - 1)


escriure_hola(4)
