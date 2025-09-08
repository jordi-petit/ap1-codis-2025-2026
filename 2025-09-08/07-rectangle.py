# programa que pinta un rectangle

import turtle

amplada = int(input("amplada? "))
alçada = int(input("alçada? "))

turtle.forward(amplada)
turtle.right(90)
turtle.forward(alçada)
turtle.right(90)
turtle.forward(amplada)
turtle.right(90)
turtle.forward(alçada)
turtle.right(90)  # per deixar la tortuga en el mateix estat que al principi

turtle.done()
