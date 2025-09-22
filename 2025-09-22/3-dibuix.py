# programa que pinta un poligon repetides vegades, tot rotant-lo
# (amb bucles for)

import turtle

costats = 4
mida = 50
nombre = 12

for j in range(1, nombre + 1):
    for i in range(1, costats + 1):
        turtle.forward(mida)
        turtle.right(360 / costats)
    turtle.right(360 / nombre)

turtle.done()
